import os
import httpx
from fastapi import HTTPException
from typing import Optional, List
from aioredis import Redis
from pydantic import BaseModel, Field
from schemas import SummaryResponse, DocumentationResponse, RecommendationResponse

AUDIO_PROCESSING_SERVICE_URL = os.getenv('AUDIO_PROCESSING_SERVICE_URL', 'http://localhost:8001')
SUMMARIZATION_SERVICE_URL = os.getenv('SUMMARIZATION_SERVICE_URL', 'http://localhost:8002')


async def get_processing_status(session_id: str, redis: Redis) -> Optional[str]:
    status = await redis.get(f"processing_status:{session_id}")
    return status if status else None


async def get_transcription(session_id: str, recording_id: str, redis: Redis) -> dict:
    # Retrieve the transcriptions in order (low to high)
    transcriptions = await redis.zrange(
        f"transcription:{session_id}:{recording_id}",
        0, -1  # Retrieve all elements
    )

    # Concatenate all the transcriptions into a single string
    transcription = ''.join(t for t in transcriptions)

    # Check if the transcription is complete
    processing_status = await redis.get(f"processing_status:{session_id}:{recording_id}")
    is_complete = processing_status == b"COMPLETED"

    return {
        "transcription": transcription,
        "is_complete": is_complete
    }


async def generate_summary(transcription: str, notes: list[str]) -> SummaryResponse:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{SUMMARIZATION_SERVICE_URL}/summarize",
                json={"transcription": transcription, "notes": notes}
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=500, detail=f"Summarization service error: {str(e)}")


async def generate_recommendations(transcription: str, notes: list[str]) -> RecommendationResponse:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{SUMMARIZATION_SERVICE_URL}/infer_new_conditions",
                json={"transcription": transcription, "notes": notes}
            )
            print('Got recommendations response:', response.json())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=500, detail=f"Summarization service error: {str(e)}")


# Keep other existing functions in external_services.py
async def initiate_audio_processing(session_id: str, recording_id: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{AUDIO_PROCESSING_SERVICE_URL}/recording",
                json={
                    "action": "initialize",
                    "sessionId": session_id,
                    "recordingId": recording_id
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=500, detail=f"Audio processing service error: {str(e)}")


async def update_audio_processing(session_id: str, recording_id: str, action: str, timestamp: float = None,
                                  position: int = None):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{AUDIO_PROCESSING_SERVICE_URL}/recording",
                json={
                    "action": action,
                    "sessionId": session_id,
                    "recordingId": recording_id,
                    "timestamp": timestamp,
                    "position": position
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=500, detail=f"Audio processing service error: {str(e)}")


async def create_documentation(transcriptions: List[str], notes: List[str],
                               summaries: List[str]) -> DocumentationResponse:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{SUMMARIZATION_SERVICE_URL}/create_documentation",
                json={
                    "transcriptions": transcriptions,
                    "notes": notes,
                    "summaries": summaries
                },
                timeout=httpx.Timeout(15.0)
            )
            response.raise_for_status()
            return DocumentationResponse(**response.json())
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=500, detail=f"Documentation creation error: {str(e)}")
