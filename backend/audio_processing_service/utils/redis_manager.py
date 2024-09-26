import aioredis
import asyncio
import logging
from config import REDIS_URL, REDIS_MAX_RETRIES, REDIS_RETRY_INTERVAL

logger = logging.getLogger(__name__)


class RedisManager:
    def __init__(self):
        self.redis_client = None

    async def init_redis_client(self):
        for attempt in range(REDIS_MAX_RETRIES):
            try:
                self.redis_client = await aioredis.from_url(REDIS_URL, decode_responses=True)
                await self.redis_client.ping()
                logger.info("Successfully connected to Redis")
                return
            except aioredis.RedisError as e:
                logger.error(f"Failed to connect to Redis (attempt {attempt + 1}/{REDIS_MAX_RETRIES}): {str(e)}")
                if attempt < REDIS_MAX_RETRIES - 1:
                    await asyncio.sleep(REDIS_RETRY_INTERVAL)

        raise Exception("Failed to connect to Redis after multiple attempts")

    async def close_redis_client(self):
        if self.redis_client:
            await self.redis_client.close()
            self.redis_client = None
            logger.info("Redis connection closed")

    async def get_redis_client(self) -> aioredis.Redis:
        if self.redis_client is None:
            await self.init_redis_client()
        return self.redis_client

    async def check_redis_connection(self):
        try:
            await self.redis_client.ping()
            return True
        except (aioredis.RedisError, AttributeError):
            return False


redis_manager = RedisManager()
