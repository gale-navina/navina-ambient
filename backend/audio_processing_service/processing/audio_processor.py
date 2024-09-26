import asyncio
import numpy as np
import logging
from models.audio_buffer import AudioBuffer
from models.enums import RecordingStatus, ProcessingStatus
from utils.kinesis_utils import get_kinesis_shard_iterator, get_kinesis_records
from processing.vad_processor import VADProcessor
from processing.transcription_processor import TranscriptionProcessor
import base64
import os
import uuid
import aioredis

logger = logging.getLogger(__name__)


class AudioProcessor:
    def __init__(self, session_id: str, recording_id: str, redis_client: aioredis.Redis):
        self.session_id = session_id
        self.recording_id = recording_id
        self.audio_buffer = AudioBuffer()
        self.vad_processor = VADProcessor()
        self.transcription_processor = TranscriptionProcessor(redis_client)
        self.redis_client = redis_client

    async def process_audio_stream(self):
        try:
            shard_iterator = await get_kinesis_shard_iterator(self.session_id, self.recording_id, self.redis_client)
            logger.info(f"Started processing for session_id={self.session_id}, recording_id={self.recording_id}")

            while self.audio_buffer.recording_status != RecordingStatus.ENDED:
                if self.audio_buffer.recording_status == RecordingStatus.PAUSED:
                    await self._handle_paused_state()
                    continue

                await self.redis_client.set(f"processing_status:{self.session_id}",
                                            ProcessingStatus.ACTIVE.value)

                records = await get_kinesis_records(shard_iterator)
                for record in records['Records']:
                    if record['PartitionKey'] == self.recording_id:
                        self._process_kinesis_record(record)

                shard_iterator = records['NextShardIterator']
                await self.redis_client.set(f"kinesis_checkpoint:{self.session_id}:{self.recording_id}", shard_iterator)

                await self._process_buffer()

                self.audio_buffer.recording_status = RecordingStatus(
                    await self.redis_client.get(f"recording_status:{self.session_id}:{self.recording_id}")
                )

                await asyncio.sleep(1)

            # Process any remaining buffer after the recording has ended
            if self.audio_buffer.get_unprocessed_samples() > 0:
                await self._process_buffer(force_process=True)

            await self._finalize_processing()

        except Exception as e:
            await self._handle_error(str(e))
        finally:
            await self._cleanup()

    def _process_kinesis_record(self, record):
        try:
            decoded_data = self._decode_kinesis_data(record['Data'])
            new_data = np.frombuffer(decoded_data, dtype=np.int16).reshape(-1, self.audio_buffer.CHANNELS)
            self.audio_buffer.append(new_data)
            logger.info(
                f"Processed Kinesis record, new buffer length: {self.audio_buffer.get_total_samples()} samples")
        except Exception as e:
            logger.error(f"Error processing Kinesis record: {str(e)}")

    async def _process_buffer(self, force_process: bool = False):
        try:
            vad_results = await self.vad_processor.process(self.audio_buffer, force_process)
            await self.transcription_processor.process(self.session_id, self.recording_id, self.audio_buffer,
                                                       force_process)
        except Exception as e:
            logger.error(f"Error processing buffer: {str(e)}")

    async def _handle_paused_state(self):
        await self.redis_client.set(f"processing_status:{self.session_id}",
                                    ProcessingStatus.PAUSED.value)
        await asyncio.sleep(1)
        self.audio_buffer.recording_status = RecordingStatus(
            await self.redis_client.get(f"recording_status:{self.session_id}:{self.recording_id}")
        )
        logger.info(f"Handling paused state for session_id={self.session_id}, recording_id={self.recording_id}")

    async def _finalize_processing(self):
        await self.redis_client.set(f"processing_status:{self.session_id}",
                                    ProcessingStatus.COMPLETED.value)
        await self.redis_client.delete(f"kinesis_checkpoint:{self.session_id}:{self.recording_id}")
        logger.info(f"Finalized processing for session_id={self.session_id}, recording_id={self.recording_id}")

    async def _handle_error(self, error_message):
        await self.redis_client.set(f"processing_status:{self.session_id}",
                                    ProcessingStatus.ERROR.value)
        logger.error(
            f"Error in AudioProcessor for session_id={self.session_id}, recording_id={self.recording_id}: {error_message}")

    async def _cleanup(self):
        await self.redis_client.delete(f"processing_instance:{self.session_id}:{self.recording_id}")
        logger.info(f"Cleanup completed for session_id={self.session_id}, recording_id={self.recording_id}")

    @staticmethod
    def _decode_kinesis_data(encoded_data):
        try:
            # Decode the Base64 data
            decoded_data = base64.b64decode(encoded_data)

            # Check if padding is needed
            if len(decoded_data) % 4 != 0:
                logger.warning(f"Decoded data length not divisible by 4: {len(decoded_data)} bytes")
                padding = 4 - (len(decoded_data) % 4)
                decoded_data += b'\x00' * padding

            return decoded_data
        except Exception as e:
            logger.error(f"Error decoding Kinesis data: {str(e)}")
            raise

    @staticmethod
    def get_instance_id():
        return os.getenv('INSTANCE_ID', str(uuid.uuid4()))
