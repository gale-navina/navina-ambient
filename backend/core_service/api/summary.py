from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models, schemas

router = APIRouter()


@router.put("/sessions/{session_id}/summary")
async def create_summary(session_id: str, summary_items: List[schemas.SummaryItem], db: Session = Depends(get_db)):
    db_session = db.query(models.Session).filter(models.Session.id == session_id).first()
    if db_session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    db_session.summary = summary_items
    db.commit()
    return {"status": "Summary created"}


@router.get("/sessions/{session_id}/summary", response_model=schemas.SummaryResponse)
async def get_summary(session_id: str, db: Session = Depends(get_db)):
    db_session = db.query(models.Session).options(joinedload(models.Session.summary)).filter(
        models.Session.id == session_id).first()
    if db_session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    if not db_session.summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return schemas.SummaryResponse(summary=db_session.summary)


@router.post("/sessions/{session_id}/summary_item", response_model=schemas.SummaryItem)
async def create_summary_item(session_id: str, summary_item: schemas.SummaryItemCreate, db: Session = Depends(get_db)):
    db_session = db.query(models.Session).options(joinedload(models.Session.summary)).filter(
        models.Session.id == session_id).first()
    if db_session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    if not db_session.summary:
        db_session.summary = []
    db_summary_item = models.SummaryItem(**summary_item.dict(), session_id=session_id)
    db.add(db_summary_item)
    db.commit()
    return db_summary_item


@router.put("/sessions/{session_id}/summary_item/{summary_item_id}", response_model=schemas.SummaryItem)
async def update_summary_item(session_id: str, summary_item_id: str, summary_item: schemas.SummaryItemCreate,
                              db: Session = Depends(get_db)):
    db_summary_item = db.query(models.SummaryItem).filter(models.SummaryItem.id == summary_item_id).first()
    if db_summary_item is None:
        raise HTTPException(status_code=404, detail="Summary item not found")
    if db_summary_item.session_id != session_id:
        raise HTTPException(status_code=400, detail="Summary item does not belong to the session")
    setattr(db_summary_item, "content", summary_item.content)
    db.commit()
    db.refresh(db_summary_item)
    return db_summary_item


@router.delete("/sessions/{session_id}/summary_item/{summary_item_id}")
async def delete_summary_item(session_id: str, summary_item_id: str, db: Session = Depends(get_db)):
    db_summary_item = db.query(models.SummaryItem).filter(models.SummaryItem.id == summary_item_id).first()
    if db_summary_item is None:
        raise HTTPException(status_code=404, detail="Summary item not found")
    if db_summary_item.session_id != session_id:
        raise HTTPException(status_code=400, detail="Summary item does not belong to the session")
    db.delete(db_summary_item)
    db.commit()
    return {"status": "Summary item deleted"}
