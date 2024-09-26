import asyncio
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from database import get_db
import models, schemas
from utils.general import get_redis, generate_token
from logger import logger
from services.external_services import get_processing_status, get_transcription, generate_summary

router = APIRouter()


@router.post("/sessions", response_model=schemas.SessionResponse)
async def create_session(session: schemas.SessionCreate, redis=Depends(get_redis),
                         db: Session = Depends(get_db)):
    # Check if the visit exists
    visit = db.query(models.Visit).filter(models.Visit.sid == session.visit_id).first()
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")

    session_id = generate_token()
    token = generate_token()
    await redis.setex(f"token:{session_id}", 60, token)  # 60 seconds TTL

    try:
        db_session = models.Session(id=session_id, visit_id=visit.id, status=schemas.SessionStatus.ACTIVE)
        db.add(db_session)
        db.commit()
    except IntegrityError:
        db.rollback()
        logger.error(f"Failed to create session for visit {session.visit_id}")
        raise HTTPException(status_code=400, detail="Failed to create session. The visit might not exist.")

    return schemas.SessionResponse(sessionId=session_id, pairingToken=token)


@router.get("/sessions/{session_id}", response_model=schemas.Session)
def get_session(session_id: str, db: Session = Depends(get_db)):
    session = db.query(models.Session).options(
        joinedload(models.Session.notes),
        joinedload(models.Session.recording)
    ).filter(models.Session.id == session_id).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return session


async def process_session_completion(session_id: str, recording_exists: bool, db: Session, redis):
    try:
        # Wait for processing to complete with a 60-second timeout
        async def wait_for_processing():
            logger.info(f"Waiting for processing to complete for session {session_id}")
            start_time = asyncio.get_event_loop().time()
            while True:
                status = await get_processing_status(session_id, redis)
                logger.info(f"Processing status for session {session_id}: {status}")
                if status == schemas.ProcessingStatus.COMPLETED.value:
                    return True
                if asyncio.get_event_loop().time() - start_time > 60:
                    return False
                await asyncio.sleep(2)  # Check every 2 seconds

        # Check if recording exists we need to wait for processing
        if recording_exists:

            processing_completed = await wait_for_processing()

            if not processing_completed:
                raise TimeoutError("Processing did not complete within 60 seconds")

            # Get transcription
            recording = db.query(models.Recording).filter(models.Recording.session_id == session_id).first()
            if not recording:
                raise HTTPException(status_code=404, detail="Recording not found")

            transcription_data = await get_transcription(session_id, recording.id, redis)

        else:
            transcription_data = {"transcription": ""}
            logger.info(f"No recording found for session {session_id} setting processing status to COMPLETED")
            await redis.set(f"processing_status:{session_id}", schemas.ProcessingStatus.COMPLETED.value)

        # Get notes
        notes = db.query(models.Note).filter(models.Note.session_id == session_id).all()
        note_contents = [note.content for note in notes]

        # Generate summary
        summary_data = await generate_summary(transcription_data["transcription"], note_contents)
        summpary_items = [models.SummaryItem(content=item, session_id=session_id) for item in summary_data["summary"]]

        # Update session in database
        logger.info(f"Updating session {session_id} with transcription and summary in database")
        db_session = db.query(models.Session).filter(models.Session.id == session_id).first()
        db_session.status = schemas.SessionStatus.COMPLETED
        db_session.transcription = transcription_data["transcription"]
        db_session.summary = summpary_items
        logger.info(f"Session new summary: {[item.content for item in summpary_items]}")
        db.commit()

        logger.info(f"Session {session_id} completed successfully")

    except TimeoutError as e:
        logger.error(f"Session {session_id} processing timed out: {str(e)}")
        db_session = db.query(models.Session).filter(models.Session.id == session_id).first()
        db_session.status = schemas.SessionStatus.FAILED
        db.commit()

    except Exception as e:
        logger.error(f"Error completing session {session_id}: {str(e)}")
        db_session = db.query(models.Session).filter(models.Session.id == session_id).first()
        db_session.status = schemas.SessionStatus.FAILED
        db.commit()


@router.post("/sessions/{session_id}/complete")
async def complete_session(session_id: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db),
                           redis=Depends(get_redis)):
    db_session = (db.query(models.Session).options(joinedload(models.Session.recording)).filter(
        models.Session.id == session_id).first())

    if db_session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    # Set status to COMPLETING
    db_session.status = schemas.SessionStatus.COMPLETING
    db.commit()

    recording_exists = db_session.recording is not None

    # Start the completion process in the background
    logger.info(f"Starting background task to complete session {session_id}")
    background_tasks.add_task(process_session_completion, session_id, recording_exists, db, redis)

    return {"status": "Session completion started"}


@router.post("/sessions/{session_id}/fail")
def fail_session(session_id: str, db: Session = Depends(get_db)):
    db_session = db.query(models.Session).filter(models.Session.id == session_id).first()
    if db_session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    db_session.status = schemas.SessionStatus.FAILED
    db.commit()
    return {"status": "Session marked as failed"}


@router.get("/sessions/{session_id}/recording", response_model=schemas.RecordingBase)
async def get_session_recordings(session_id: str, db: Session = Depends(get_db)):
    recording = db.query(models.Recording).filter(models.Recording.session_id == session_id).first()
    return schemas.RecordingResponse(recordingId=recording.id, status=recording.status)
