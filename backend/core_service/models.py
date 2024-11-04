from sqlalchemy import Column, String, Text, ForeignKey, DateTime, Enum, JSON
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import schemas
import uuid


class Visit(Base):
    __tablename__ = "visits"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    sid = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    sessions = relationship("Session", back_populates="visit")
    documentation = relationship("Documentation", back_populates="visit", uselist=False)


class Session(Base):
    __tablename__ = "sessions"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    visit_id = Column(String, ForeignKey("visits.id"))
    transcription = Column(Text)
    status = Column(Enum(schemas.SessionStatus), default=schemas.SessionStatus.ACTIVE)
    created_at = Column(DateTime, default=datetime.utcnow)
    visit = relationship("Visit", back_populates="sessions")
    notes = relationship("Note", back_populates="session")
    summary = relationship("SummaryItem", back_populates="session")
    recommendations = relationship("Recommendation", back_populates="session")
    recording = relationship("Recording", back_populates="session", uselist=False)


class Note(Base):
    __tablename__ = "notes"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, ForeignKey("sessions.id"))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    session = relationship("Session", back_populates="notes")


class SummaryItem(Base):
    __tablename__ = "summary_items"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, ForeignKey("sessions.id"))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    session = relationship("Session", back_populates="summary")


class Documentation(Base):
    __tablename__ = "documentations"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    visit_id = Column(String, ForeignKey("visits.id"), unique=True)
    hpi = Column(Text)
    pe = Column(Text)
    anp = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    visit = relationship("Visit", back_populates="documentation")


class Recording(Base):
    __tablename__ = "recordings"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, ForeignKey("sessions.id"), unique=True)  # One-to-one relationship
    status = Column(Enum(schemas.RecordingStatus), default=schemas.RecordingStatus.INITIALIZED)
    created_at = Column(DateTime, default=datetime.utcnow)
    session = relationship("Session", back_populates="recording", uselist=False)


class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, ForeignKey("sessions.id"))
    content = Column(JSON)
    session = relationship("Session", back_populates="recommendations")
