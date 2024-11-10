from pydantic import BaseModel, Field, model_validator
from typing import Optional, List
from datetime import datetime
import enum


# related schemas for Note
class Note(BaseModel):
    session_id: str
    id: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class NoteCreate(BaseModel):
    content: str


# related schemas for SummaryItem
class SummaryItem(BaseModel):
    session_id: str
    id: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class SummaryItemCreate(BaseModel):
    content: str


# related schemas for Recording
class RecordingStatus(str, enum.Enum):
    INITIALIZED = "initialized"
    ACTIVE = "active"
    PAUSED = "paused"
    ENDED = "ended"
    ERROR = "error"


class RecordingAction(str, enum.Enum):
    START = "start"
    STOP = "stop"
    PAUSE = "pause"
    RESUME = "resume"


class RecordingRequest(BaseModel):
    sessionId: str
    recordingId: str
    action: RecordingAction
    timestamp: Optional[float] = None
    position: Optional[int] = None


class RecordingBase(BaseModel):
    id: str
    status: RecordingStatus


class SessionStatus(str, enum.Enum):
    ACTIVE = "active"
    COMPLETING = "completing"
    COMPLETED = "completed"
    FAILED = "failed"


class Recommendation(BaseModel):
    id: str
    session_id: str
    content: dict


class Session(BaseModel):
    id: str
    transcription: Optional[str] = None
    summary: Optional[List[SummaryItem]] = []
    recommendations: Optional[List[Recommendation]] = []
    status: SessionStatus
    created_at: datetime
    notes: List[Note] = []
    recording: Optional[RecordingBase] = None

    class Config:
        orm_mode = True


class ConditionOption(BaseModel):
    name: str = Field(..., description="The name of the condition from the ICD database.")
    icd_code: str = Field(..., description="The ICD code for the condition.")


class AssessmentAndPlan(BaseModel):
    condition_options: List[ConditionOption] = Field(
        ...,
        description="A list of possible conditions that the patient may have. Aim for multiple options of different hierarchy and specificity."
    )
    chosen_condition_index: int = Field(
        ..., description="The index of the chosen condition from the list of possible conditions."
    )
    title: Optional[str] = Field(
        None, description="The title of the chosen condition. defaults to '[condition.name] ([condition.icd_code])'."
    )
    assessment_and_plan: str = Field(
        ...,
        description="The current condition assessment and treatment or follow-up plan for the condition if such provided."
    )
    already_documented: bool = Field(False,
                                     description="Whether the condition is already documented in the patient's record.")

    @model_validator(mode="before")
    def set_default_title(cls, values):
        # Check if 'title' is not provided
        if not values.get('title'):
            # Fetch the chosen condition from condition_options based on chosen_condition_index
            chosen_index = values.get('chosen_condition_index')
            if chosen_index is not None and 0 <= chosen_index < len(values.get('condition_options', [])):
                selected_option = values['condition_options'][chosen_index]
                # Set the default title using the selected option's name and ICD code
                values['title'] = f"{selected_option['name']} ({selected_option['icd_code']})"
        return values


class RecommendationResponse(BaseModel):
    recommendations: List[AssessmentAndPlan]


class DocumentedCondition(BaseModel):
    condition: str
    icd_code: str
    current_anp: str


class DocumentationResponse(BaseModel):
    hpi: Optional[str] = Field(None,
                               description="History of Present Illness (HPI), summarizing the patient's current condition.")
    pe: Optional[str] = Field(None,
                              description="Physical Examination (PE), summarizing the findings from the physical exam.")
    anp: Optional[List[AssessmentAndPlan]] = Field(None,
                                                   description="The Assessment and Plan (A&P) for the patient, with possible ICD codes (at least 3) and treatment plan.")


class Documentation(BaseModel):
    visit_id: str
    id: str
    hpi: Optional[str] = Field(None,
                               description="History of Present Illness (HPI), summarizing the patient's current condition.")
    pe: Optional[str] = Field(None,
                              description="Physical Examination (PE), summarizing the findings from the physical exam.")
    anp: Optional[List[AssessmentAndPlan]] = Field(None,
                                                   description="The Assessment and Plan (A&P) for the patient, with possible ICD codes and treatment plan.")

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class DocumentationCreate(BaseModel):
    visit_id: str
    current_conditions: List[DocumentedCondition]


class DocumentationUpdate(BaseModel):
    hpi: Optional[str] = None
    pe: Optional[str] = None
    anp: Optional[List[AssessmentAndPlan]] = None


class SessionCreate(BaseModel):
    visit_id: str


class SessionResponse(BaseModel):
    sessionId: str
    pairingToken: str


class VisitBase(BaseModel):
    sid: str


class VisitCreate(VisitBase):
    pass


class Visit(VisitBase):
    id: str
    created_at: datetime
    sessions: List[Session] = []
    documentation: Optional[Documentation] = None

    class Config:
        orm_mode = True


class PairingRequest(BaseModel):
    sessionId: str
    token: str


class PairingResponse(BaseModel):
    recordingId: str
    streamUrl: str
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str
    expiration: str


class ProcessingStatus(str, enum.Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    FINALIZING = "finalizing"
    ERROR = "error"


class TranscriptionResponse(BaseModel):
    transcription: str
    is_complete: bool


class SummaryResponse(BaseModel):
    summary: List[SummaryItem]


class PutSummaryRequest(BaseModel):
    summary: List[SummaryItem]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: Optional[str] = None


class UserInDB(User):
    hashed_password: str
