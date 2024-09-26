import aioredis
import os
import uuid
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from models import Base


def wait_for_db(db_uri, max_retries=30, retry_interval=2):
    retries = 0
    while retries < max_retries:
        try:
            engine = create_engine(db_uri)
            with engine.connect():
                return engine  # Return the engine if successfully connected
        except OperationalError:
            retries += 1
            print(
                f"Attempt {retries}/{max_retries} to connect to the database failed. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)

    raise Exception("Could not connect to the database after maximum retries")


def create_tables(engine):
    Base.metadata.create_all(engine)
    print("Tables created successfully")


def initialize_database(db_uri):
    engine = wait_for_db(db_uri)
    create_tables(engine)
    return engine


async def get_redis():
    redis = await aioredis.from_url(os.getenv('REDIS_URL', 'redis://localhost'), encoding="utf-8",
                                    decode_responses=True)
    try:
        yield redis
    finally:
        await redis.close()


def generate_token():
    return str(uuid.uuid4())
