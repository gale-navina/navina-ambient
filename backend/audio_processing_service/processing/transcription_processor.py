import asyncio
import tempfile
import os
import soundfile as sf
import openai
import logging
import numpy as np
from models.audio_buffer import AudioBuffer
from config import (
    MAX_CONCURRENT_TRANSCRIPTIONS, OPENAI_API_KEY,
    SAMPLE_RATE
)
import aioredis

logger = logging.getLogger(__name__)


class TranscriptionProcessor:
    def __init__(self, redis_client: aioredis.Redis):
        self.openai_client = openai.Client(api_key=OPENAI_API_KEY)
        self.transcription_semaphore = asyncio.Semaphore(MAX_CONCURRENT_TRANSCRIPTIONS)
        self.silence_threshold = 0.5  # 0.5 seconds of silence
        self.min_chunk_size = 15  # 15 seconds of audio
        self.redis_client = redis_client

    async def process(self, session_id: str, recording_id: str, audio_buffer: AudioBuffer, force_process=False):
        silence_threshold_samples = int(self.silence_threshold * SAMPLE_RATE)
        min_chunk_size_samples = self.min_chunk_size * SAMPLE_RATE

        silence_periods = self._find_all_silence(audio_buffer, silence_threshold_samples)
        logger.info(f"Found {len(silence_periods)} silence periods in VAD results")

        if force_process and (not silence_periods or silence_periods[-1] < len(audio_buffer.vad_results)):
            silence_periods.append(len(audio_buffer.vad_results))

        for silence_end in silence_periods:
            chunk_size = silence_end - audio_buffer.last_transcribed_sample

            if chunk_size >= min_chunk_size_samples or (force_process and (silence_end == len(audio_buffer.vad_results))):
                chunk = audio_buffer.get_chunk(audio_buffer.last_transcribed_sample, silence_end)
                await self._transcribe_chunk(session_id, recording_id, chunk, audio_buffer.last_transcribed_sample)
                audio_buffer.last_transcribed_sample = silence_end
                logger.info(
                    f"Transcribed chunk for {session_id}:{recording_id}, start: {audio_buffer.last_transcribed_sample}, end: {silence_end}")

    async def _transcribe_chunk(self, session_id: str, recording_id: str, chunk: np.array, start_sample: int):
        async with self.transcription_semaphore:
            try:
                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
                    sf.write(temp_audio.name, chunk, SAMPLE_RATE, subtype='PCM_16')

                with open(temp_audio.name, "rb") as audio_file:
                    response = self.openai_client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file
                    )

                transcription = response.text
                await self.redis_client.zadd(
                    f"transcription:{session_id}:{recording_id}",
                    {transcription: start_sample / SAMPLE_RATE}
                )
                logger.info(
                    f"Transcribed chunk for {session_id}:{recording_id}, start time: {start_sample / SAMPLE_RATE}")
            except Exception as e:
                logger.error(
                    f"Error transcribing chunk for {session_id}:{recording_id}, start sample: {start_sample}: {str(e)}")
                await self.redis_client.zadd(
                    f"failed_transcriptions:{session_id}:{recording_id}",
                    {f"start_sample:{start_sample}": start_sample / SAMPLE_RATE}
                )
            finally:
                os.unlink(temp_audio.name)

    @staticmethod
    def _find_all_silence(audio_buffer: AudioBuffer, silence_threshold):
        silence_periods = []
        start_point = audio_buffer.last_transcribed_sample
        silence_start = start_point
        relevant_vad_results = audio_buffer.vad_results[silence_start:]
        for i, is_speech in enumerate(relevant_vad_results):
            if is_speech:
                silence_start = i + 1
            elif i - silence_start >= silence_threshold:
                # Go back to middle of silence period
                silence_periods.append(start_point + silence_start - silence_threshold // 2)
        return silence_periods
