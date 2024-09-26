from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models, schemas
from logger import logger
from utils.general import get_redis
from services.external_services import create_documentation as create_documentation_external

router = APIRouter()


@router.get("/visits/{sid}", response_model=schemas.Visit)
def get_visit(sid: str, db: Session = Depends(get_db)):
    logger.info(f"Fetching or creating visit with SID: {sid}")
    try:
        visit = db.query(models.Visit).options(
            joinedload(models.Visit.sessions).joinedload(models.Session.notes),
            joinedload(models.Visit.documentation)
        ).filter(models.Visit.sid == sid).first()

        if visit is None:
            logger.info(f"Visit with SID {sid} not found. Creating new visit.")
            visit = models.Visit(sid=sid)
            db.add(visit)
            db.commit()
            db.refresh(visit)
            logger.info(f"New visit created with SID: {sid}")
        else:
            logger.info(f"Existing visit found with SID: {sid}")

        # filter sessions with failed status
        visit.sessions = [session for session in visit.sessions if session.status != schemas.SessionStatus.FAILED]

        return visit
    except Exception as e:
        logger.error(f"Error fetching/creating visit with SID {sid}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/visits/{visit_id}/documentation", response_model=schemas.DocumentationResponse)
async def create_visit_documentation(visit_id: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db),
                                     redis=Depends(get_redis)):
    visit = db.query(models.Visit).filter(models.Visit.id == visit_id).first()
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")

    if visit.documentation:
        raise HTTPException(status_code=400, detail="Documentation already exists for this visit")

    # Start the documentation creation process in the background
    background_tasks.add_task(process_documentation_creation, visit_id, db, redis)

    return schemas.DocumentationResponse(status="Documentation creation started")


async def process_documentation_creation(visit_id: str, db: Session, redis):
    try:
        visit = db.query(models.Visit).filter(models.Visit.id == visit_id).first()
        if not visit:
            raise Exception(f"Visit with id {visit_id} not found")

        transcriptions = []
        notes = []
        summaries = []

        for session in visit.sessions:
            transcriptions.append(session.transcription)
            notes.extend([note.content for note in session.notes])
            summaries.extend([item.content for item in session.summary])

        logger.info(f"Creating documentation for visit {visit_id} with summary items: {summaries}")
        documentation_content = await create_documentation_external(transcriptions, notes, summaries)

        new_documentation = models.Documentation(visit_id=visit_id, content=documentation_content)
        db.add(new_documentation)
        db.commit()
        db.refresh(new_documentation)

        # Update the visit with the new documentation
        visit.documentation = new_documentation
        db.commit()

        # Update Redis to indicate documentation is ready
        await redis.set(f"documentation_status:{visit_id}", "completed")

    except Exception as e:
        logger.error(f"Error creating documentation for visit {visit_id}: {str(e)}")
        await redis.set(f"documentation_status:{visit_id}", "failed")
        db.rollback()  # Rollback the transaction if an error occurred


@router.get("/visits/{visit_id}/documentation", response_model=schemas.Documentation)
async def get_visit_documentation(visit_id: str, db: Session = Depends(get_db), redis=Depends(get_redis)):
    documentation = db.query(models.Documentation).filter(models.Documentation.visit_id == visit_id).first()
    if not documentation:
        status = await redis.get(f"documentation_status:{visit_id}")
        if status == b"completed":
            raise HTTPException(status_code=500, detail="Documentation status inconsistent")
        elif status == b"failed":
            raise HTTPException(status_code=500, detail="Documentation creation failed")
        else:
            raise HTTPException(status_code=404, detail="Documentation not found or not yet created")
    return documentation
