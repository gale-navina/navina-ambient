from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from utils.general import get_redis
from services.external_services import update_audio_processing, get_transcription, generate_summary

router = APIRouter()


@router.post("/recording", response_model=schemas.RecordingBase)
async def handle_recording(
        request: schemas.RecordingRequest,
        background_tasks: BackgroundTasks,
        db: Session = Depends(get_db),
        redis=Depends(get_redis)
):
    recording = db.query(models.Recording).filter(models.Recording.id == request.recordingId).first()  # type: ignore
    if not recording:
        raise HTTPException(status_code=404, detail="Recording not found")

    # Update local status
    if request.action == schemas.RecordingAction.START:
        recording.status = schemas.RecordingStatus.ACTIVE
    elif request.action == schemas.RecordingAction.STOP:
        recording.status = schemas.RecordingStatus.ENDED
    elif request.action == schemas.RecordingAction.PAUSE:
        recording.status = schemas.RecordingStatus.PAUSED
    elif request.action == schemas.RecordingAction.RESUME:
        recording.status = schemas.RecordingStatus.ACTIVE

    db.commit()

    # Update Redis (for real-time status)
    await redis.set(f"recording_status:{request.sessionId}:{request.recordingId}", recording.status.value)

    # Update audio processing service in the background
    background_tasks.add_task(
        update_audio_processing,
        request.sessionId,
        request.recordingId,
        request.action.value,
        request.timestamp,
        request.position
    )

    return schemas.RecordingBase(id=recording.id, status=recording.status)


@router.get("/sessions/{session_id}/recordings/{recording_id}/transcription",
            response_model=schemas.TranscriptionResponse)
async def get_recording_transcription(session_id: str, recording_id: str):
    transcription_data = await get_transcription(session_id, recording_id)
    return schemas.TranscriptionResponse(**transcription_data)


@router.post("/sessions/{session_id}/recordings/{recording_id}/summary", response_model=schemas.SummaryResponse)
async def create_summary(session_id: str, recording_id: str, db: Session = Depends(get_db)):
    # Get transcription
    transcription_data = await get_transcription(session_id, recording_id)

    # Get notes
    notes = db.query(models.Note).filter(models.Note.session_id == session_id).all()  # type: ignore
    note_contents = [note.content for note in notes]

    # Generate summary
    summary_data = await generate_summary(transcription_data["transcription"], note_contents)

    # Save summary to database
    session = db.query(models.Session).filter(models.Session.id == session_id).first()  # type: ignore
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    session.summary = summary_data["summary"]
    db.commit()

    return schemas.SummaryResponse(summary=summary_data["summary"])
