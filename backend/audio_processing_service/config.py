import os

# Kinesis configuration
KINESIS_STREAM_NAME = os.getenv('KINESIS_STREAM_NAME', 'your-kinesis-stream-name')
LOCAL_AWS_ENDPOINT = os.getenv('LOCAL_AWS_ENDPOINT', 'http://localstack:4566')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'LKIAQAAAAAAAEFINJXXD')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'Sir9d3Vwg/aWKhI76TutiQZVH7fQc11hwMM8Ln8M')

# Redis configuration
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost')
REDIS_MAX_RETRIES = int(os.getenv('REDIS_MAX_RETRIES', '5'))
REDIS_RETRY_INTERVAL = int(os.getenv('REDIS_RETRY_INTERVAL', '5'))

# Audio processing configuration
SAMPLE_RATE = 16000
CHANNELS = 1
BYTES_PER_SAMPLE = 2  # 16-bit samples
BYTES_PER_SECOND = SAMPLE_RATE * CHANNELS * BYTES_PER_SAMPLE
SEGMENTATION_FRAME_DURATION = 10  # seconds
SEGMENTATION_CHUNK_SIZE = SEGMENTATION_FRAME_DURATION * BYTES_PER_SECOND
EXPECTED_LENGTH = 2.5  # seconds
TARGET_FRAME_RATE = 16000  # Hz

# Transcription configuration
MAX_CONCURRENT_TRANSCRIPTIONS = int(os.getenv('MAX_CONCURRENT_TRANSCRIPTIONS', '10'))
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# VAD configuration
VAD_MODEL_PATH = os.getenv('VAD_MODEL_PATH', './pyannote-segmentation-3/pytorch_model.bin')
VAD_MAX_SPEAKERS = 3
VAD_MAX_SPEAKERS_PER_FRAME = 2

# API configuration
API_TOKEN_URL = os.getenv('API_TOKEN_URL', '/token')
