import boto3
import asyncio
from datetime import datetime, timezone
import aioredis
import logging
from config import (
    KINESIS_STREAM_NAME, LOCAL_AWS_ENDPOINT, AWS_REGION,
    AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
)

logger = logging.getLogger(__name__)

kinesis_client = boto3.client('kinesis',
                              endpoint_url=LOCAL_AWS_ENDPOINT,
                              region_name=AWS_REGION,
                              aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


async def get_kinesis_shard_iterator(session_id: str, recording_id: str, redis_client: aioredis.Redis,
                                     max_retries: int = 30, delay: int = 2):
    start_time_str = await redis_client.get(f"recording_start_time:{session_id}:{recording_id}")
    if start_time_str is None:
        raise ValueError(f"Start time not found for recording_id: {recording_id}")

    start_time = float(start_time_str) - 60
    logger.info(
        f"Searching for shard iterator from start time: {start_time} for session_id={session_id}, recording_id={recording_id}")

    for attempt in range(max_retries):
        try:
            stream_description = kinesis_client.describe_stream(StreamName=KINESIS_STREAM_NAME)
            shard_ids = [shard['ShardId'] for shard in stream_description['StreamDescription']['Shards']]

            for shard_id in shard_ids:
                shard_iterator = kinesis_client.get_shard_iterator(
                    StreamName=KINESIS_STREAM_NAME,
                    ShardId=shard_id,
                    ShardIteratorType='AT_TIMESTAMP',
                    Timestamp=datetime.fromtimestamp(start_time, tz=timezone.utc)
                )['ShardIterator']

                records = kinesis_client.get_records(ShardIterator=shard_iterator)

                for record in records['Records']:
                    if record['PartitionKey'] == recording_id:
                        logger.info(f"Found shard iterator for session_id={session_id}, recording_id={recording_id}")
                        return shard_iterator

            logger.warning(
                f"No matching records found in attempt {attempt + 1} for session_id={session_id}, recording_id={recording_id}")
            # Wait before retrying
            await asyncio.sleep(delay)

        except Exception as e:
            logger.error(
                f"Error in attempt {attempt + 1} for session_id={session_id}, recording_id={recording_id}: {str(e)}")
            if attempt < max_retries - 1:
                await asyncio.sleep(delay)
            else:
                raise ValueError(f"Failed to find shard for recording_id={recording_id} after {max_retries} attempts")

    raise ValueError(f"Failed to find shard for recording_id={recording_id} after {max_retries} attempts")


async def get_kinesis_records(shard_iterator: str):
    records = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=10000)
    return records
