from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models, schemas

router = APIRouter()


@router.get("/sessions/{session_id}/notes", response_model=List[schemas.Note])
def get_notes(session_id: str, db: Session = Depends(get_db)):
    db_session = db.query(models.Session).options(joinedload(models.Session.notes)).filter(
        models.Session.id == session_id).first()
    if db_session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return db_session.notes


@router.post("/sessions/{session_id}/note", response_model=schemas.Note)
def create_note(session_id: str, note: schemas.NoteCreate, db: Session = Depends(get_db)):
    db_note = models.Note(**note.dict(), session_id=session_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


@router.put("/sessions/{session_id}/note/{note_id}", response_model=schemas.Note)
def update_note(session_id: str, note_id: str, note: schemas.NoteCreate, db: Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    if db_note.session_id != session_id:
        raise HTTPException(status_code=400, detail="Note does not belong to the session")
    setattr(db_note, "content", note.content)
    db.commit()
    db.refresh(db_note)
    return db_note


@router.delete("/sessions/{session_id}/note/{note_id}")
def delete_note(session_id: str, note_id: str, db: Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    if db_note.session_id != session_id:
        raise HTTPException(status_code=400, detail="Note does not belong to the session")
    db.delete(db_note)
    db.commit()
    return {"status": "Note deleted"}
