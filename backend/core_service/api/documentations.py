from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models, schemas
from services.external_services import create_documentation as create_documentation_external

router = APIRouter()


@router.post("/documentations", response_model=schemas.Documentation)
async def create_documentation(documentation_request: schemas.DocumentationCreate, db: Session = Depends(get_db)):
    db_visit = db.query(models.Visit).options(joinedload(models.Visit.documentation)).filter(
        models.Visit.sid == documentation_request.visit_id).first()
    if db_visit is None:
        raise HTTPException(status_code=404, detail="Visit not found")
    # Limit to one documentation per visit
    if db_visit.documentation:
        raise HTTPException(status_code=400, detail="Documentation already exists for this visit")
    else:
        # get notes transcriptions and summaries from sessions
        all_notes = [note.content for session in db_visit.sessions for note in session.notes]
        all_transcriptions = [session.transcription for session in db_visit.sessions if session.transcription]
        all_summaries = [item.content for session in db_visit.sessions for item in session.summary]
        documentation_ext_response = await create_documentation_external(all_notes, all_transcriptions, all_summaries)
    db_documentation = models.Documentation(visit_id=db_visit.id, **documentation_ext_response.dict())
    db.add(db_documentation)
    db.commit()
    db.refresh(db_documentation)
    return db_documentation


@router.put("/documentations/{visit_id}", response_model=schemas.Documentation)
def update_documentation(visit_id: str, documentation: schemas.DocumentationUpdate, db: Session = Depends(get_db)):
    db_visit = db.query(models.Visit).options(joinedload(models.Visit.documentation)).filter(
        models.Visit.sid == visit_id).first()
    if db_visit is None:
        raise HTTPException(status_code=404, detail="Visit not found")
    db_documentation = db_visit.documentation
    if db_documentation is None:
        raise HTTPException(status_code=404, detail="Documentation not found")
    for key, value in documentation.dict().items():
        setattr(db_documentation, key, value)
    db.commit()
    db.refresh(db_documentation)
    return db_documentation
