import os
from typing import List, Optional, Any
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, Field
from openai import OpenAI
from logger import logger

from auto_documentation.types import AssessmentResponse
from auto_documentation.documentation import document_raw_summary_request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify domains ['http://localhost:3000']
    allow_credentials=True,
    allow_methods=["*"],  # or just ['POST']
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {str(exc)}", exc_info=True)
    error_location = f"{exc.__class__.__name__} at {exc.__traceback__.tb_frame.f_code.co_filename}:{exc.__traceback__.tb_lineno}"
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal Server Error",
            "message": str(exc),
            "error_location": error_location
        }
    )


class DocumentedCondition(BaseModel):
    condition: str = Field(..., description="The name of the condition.")
    icd_code: str = Field(..., description="The ICD code for the condition.")
    current_anp: str = Field(..., description="The current assessment and plan for the condition.")


class SummarizationRequest(BaseModel):
    transcription: str
    notes: List[str] = []


class SummarizationResponse(BaseModel):
    summary: List[str] = Field(...,
                               description="List of individual concise medical points that create a cohesive summary of the session.")


class ConditionOption(BaseModel):
    name: str = Field(..., description="The name of the condition from the ICD database.")
    icd_code: str = Field(..., description="The ICD code for the condition.")


class AssessmentAndPlan(BaseModel):
    condition_options: List[ConditionOption] = Field(...,
                                                     description="A list of possible conditions that the patient may have. Aim for multiple options of different hirarchy and specificity.")
    chosen_condition_index: int = Field(...,
                                        description="The index of the chosen condition from the list of possible conditions.")
    assessment_and_plan: str = Field(...,
                                     description="Assessment of current condition state and the treatment or follow-up plan if such exists. If already documented, only include new text that will be appended to the existing documentation.")
    already_documented: bool = Field(...,
                                     description="Whether the condition is already documented in the patient's record.")


class RecommendationResponse(BaseModel):
    recommendations: List[AssessmentAndPlan] = Field(...,
                                                     description="List of possible conditions that the patient may have. Aim for multiple options of different hirarchy and specificity.")


class AutoDocumentationResponse(BaseModel):
    diagnosis: ConditionOption = Field(..., description="The diagnosis for the patient.")
    assessment: str = Field(..., description="Assessment of the patient's current condition.")


class DocumentationResponse(BaseModel):
    hpi: Optional[str] = Field(None,
                               description="History of Present Illness (HPI), summarizing the patient's current condition.")
    pe: Optional[str] = Field(None,
                              description="Physical Examination (PE), summarizing the findings from the physical exam.")
    anp: Optional[List[AssessmentAndPlan]] = Field(None,
                                                   description="The Assessment and Plan (A&P) for the patient, with possible ICD codes (at least 3) and treatment plan.")


class DocumentationRequest(BaseModel):
    transcriptions: List[str]
    notes: List[str]
    summaries: List[str]
    current_conditions: List[DocumentedCondition]


class SuggestionsDocumentationRequest(BaseModel):
    suggestions: List[Any]
    base_labs: List[Any]
    all_labs: List[Any]
    meds: List[Any]
    family_history: List[Any]
    social_history: Optional[Any] = None


@app.post("/summarize", response_model=SummarizationResponse)
async def summarize_transcription(request: SummarizationRequest):
    try:
        combined_text = f"{request.transcription}\n\nNotes:\n" + "\n".join(request.notes)
        print("sending request to openai")
        response = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system",
                 "content": "You are a medical assistant tasked with summarizing patient-doctor conversations and associated notes."},
                {"role": "user",
                 "content": f"""
                 Create a medical transcript summary that preserves the content discussed during the visit and the medical notes by the doctor.\n\n 
                 Provide simple text with concice summary that includes all parts of the visit up to 20 sentences.\n\n 
                 Use Only the following data:\n\n{combined_text}\n\n
                 Do not add any information that is not provided in the input data.
                 Prefer short or empty response if input data is not sufficient for a summary.
                 """
                 }
            ],
            response_format=SummarizationResponse,
            max_tokens=300,
            n=1,
            stop=None,
            temperature=0
        )
        print('Got response:', response.choices[0].message.parsed)

        structured_summary = response.choices[0].message.parsed
        return structured_summary
    except Exception as e:
        logger.error(f"Error summarizing transcription: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/infer_new_conditions", response_model=RecommendationResponse)
async def infer_new_conditions(request: SummarizationRequest):
    try:
        response = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system",
                 "content": "You are a medical assistant tasked with documenting given medical data for conditions and treatment plans if the plan was established by a doctor."},
                {"role": "user",
                 "content": f"""
                 For the main new condition / conditions that where mentioned during this medical session:
                 For each condition, assign a condition name and its corresponding ICD code (if uncertain, provide a list of possible ICD codes). 
                 Follow this with a detailed assessment for that condition and the treatment plan only if such provided in data by the doctor.\n\n
                 {request.transcription}\n\nNotes:\n{request.notes}
                 Do not add any information that is not provided in the input data, if no plan is provided by the doctor, include only assessment of current condition state.
                 """
                 }
            ],
            response_format=RecommendationResponse,
            max_tokens=300,
            n=1,
            stop=None,
            temperature=0
        )
        structured_response = response.choices[0].message.parsed
        return structured_response
    except Exception as e:
        logger.error(f"Error inferring new conditions: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/create_documentation", response_model=DocumentationResponse)
async def create_documentation(request: DocumentationRequest):
    try:
        combined_text = "\n".join([
            "Visit Transcriptions:",
            *request.transcriptions,
            "\n",
            "Visit Notes:",
            *request.notes,
            "\n",
            "Visit Summaries:",
            *request.summaries,
            "\n",
            "Current Documented Conditions To Include:",
            *[
                f"Condition: {condition.condition} | ICD Code: {condition.icd_code} | Current Assessment: {condition.current_anp}"
                for condition in
                request.current_conditions]
        ])

        print("sending request to openai", combined_text)

        response = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": "You are a medical assistant responsible for creating precise and concise medical documentation based solely on provided transcriptions, notes, and summaries from patient visits. Do not fabricate or infer any information. Use only the provided data in its entirety to create the documentation."
                },
                {
                    "role": "user",
                    "content": f"""
                    Please create a unified concise medical document with the following structured sections, and omit any sections for which no data is provided.
                    Format the documentation as follows:\n\n
                    1. **HPI**: History of Present Illness, typically 1-2 paragraphs summarizing the patient's current condition and symptoms.\n\n
                    2. **PE**: Physical Examination, summarized in a single paragraph with one row per system reviewed (e.g., cardiovascular, respiratory, etc.).\n\n
                    3. **Assessment and Plan**:  Create a list of all patients conditions rather they are already documented or aride from new data. For not documented condition: include condition name and its corresponding ICD code (if uncertain, provide a list of possible ICD codes). Follow this with a detailed assessment for that condition  and a treatment plan only if such provided by the doctor.\n
                    For conditions that are already documented: include current condition name and icd code, only include *new text that will be appended* to the existing documentation if such exist. state that the condition is already documeted in the relevant flag field.\n\n
                    Use only the following information:\n\n
                    {combined_text}.\n\n\n\n
                    Do not add any physical exam, result, diagnosis, or assamet and plan information that is not provided explicitly in the input data by the doctor.
                    """
                }
            ],
            response_format=DocumentationResponse,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0
        )

        # Extract and return the structured response
        structured_response = response.choices[0].message.parsed
        return structured_response  # Return the parsed structured JSON

    except Exception as e:
        logger.error(f"Error creating documentation: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/suggestions_documentation")
async def document_suggestions(request: SuggestionsDocumentationRequest):
    try:
        print('start document_suggestions')
        raw_data = request.model_dump()
        print('successfully dumped model')
        return await document_raw_summary_request(raw_summary_data=raw_data)

    except Exception as e:
        logger.error(f"Error suggesting documentation: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
