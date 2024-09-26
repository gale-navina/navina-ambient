from fastapi import APIRouter, BackgroundTasks, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from models.enums import RecordingAction, RecordingStatus, ProcessingStatus
from processing.audio_processor import AudioProcessor
from utils.redis_manager import redis_manager
import aioredis

router = APIRouter()


async def get_redis():
    return await redis_manager.get_redis_client()


class RecordingUpdate(BaseModel):
    action: RecordingAction
    sessionId: str
    recordingId: str
    timestamp: Optional[float] = None
    position: Optional[int] = None


@router.post("/recording")
async def handle_recording(
        request: RecordingUpdate,
        background_tasks: BackgroundTasks,
        redis: aioredis.Redis = Depends(get_redis)
):
    if request.action == RecordingAction.INITIALIZE:
        return await initialize_processing(request, redis)
    elif request.action == RecordingAction.START:
        return await start_processing(request, background_tasks, redis)
    elif request.action in [RecordingAction.PAUSE, RecordingAction.RESUME, RecordingAction.STOP]:
        return await update_processing(request, redis)
    else:
        raise HTTPException(status_code=400, detail="Invalid action")


async def initialize_processing(request: RecordingUpdate, redis: aioredis.Redis):
    await redis.set(f"processing_instance:{request.sessionId}:{request.recordingId}", AudioProcessor.get_instance_id())
    await redis.set(f"processing_status:{request.sessionId}", ProcessingStatus.ACTIVE.value)
    return {"status": "processing initialized"}


async def start_processing(request: RecordingUpdate, background_tasks: BackgroundTasks, redis: aioredis.Redis):
    if request.timestamp is None:
        raise HTTPException(status_code=400, detail="Timestamp is required for start action")

    current_status = await redis.get(f"recording_status:{request.sessionId}:{request.recordingId}")
    if current_status not in [RecordingStatus.ACTIVE.value, RecordingStatus.INITIALIZED.value]:
        raise HTTPException(status_code=400, detail="Recording must be initialized or active before starting")

    await redis.set(f"recording_start_time:{request.sessionId}:{request.recordingId}", request.timestamp)
    await redis.set(f"processing_status:{request.sessionId}", ProcessingStatus.ACTIVE.value)

    audio_processor = AudioProcessor(request.sessionId, request.recordingId, redis)
    background_tasks.add_task(audio_processor.process_audio_stream)

    return {"status": "Processing started", "start_time": request.timestamp}


async def update_processing(request: RecordingUpdate, redis: aioredis.Redis):
    if request.action == RecordingAction.PAUSE:
        await redis.set(f"processing_status:{request.sessionId}", ProcessingStatus.PAUSED.value)
    elif request.action == RecordingAction.RESUME:
        await redis.set(f"processing_status:{request.sessionId}", ProcessingStatus.ACTIVE.value)
    elif request.action == RecordingAction.STOP:
        await redis.set(f"processing_status:{request.sessionId}",
                        ProcessingStatus.FINALIZING.value)
    return {"status": f"Processing {request.action.value}d"}


@router.get("/recover/{session_id}/{recording_id}")
async def recover_recording(
        session_id: str,
        recording_id: str,
        background_tasks: BackgroundTasks,
        redis: aioredis.Redis = Depends(get_redis)
):
    recording_status = await redis.get(f"recording_status:{session_id}:{recording_id}")
    try:
        recording_status = RecordingStatus(recording_status)
    except ValueError:
        raise HTTPException(status_code=404, detail="Recording status not found")

    if recording_status in [RecordingStatus.ACTIVE, RecordingStatus.PAUSED, RecordingStatus.ERROR]:
        await redis.set(f"processing_instance:{session_id}:{recording_id}", AudioProcessor.get_instance_id())
        audio_processor = AudioProcessor(session_id, recording_id, redis)
        background_tasks.add_task(audio_processor.process_audio_stream)
        return {"status": "Recovery started"}
    else:
        raise HTTPException(status_code=400, detail="Recording not eligible for recovery")
