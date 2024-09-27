import os
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel, Field
from openai import OpenAI
from logger import logger

app = FastAPI()

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
    plan: str = Field(..., description="Assessment of current condition state and the treatment or follow-up plan if such exists.")


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


@app.post("/summarize", response_model=SummarizationResponse)
async def summarize_transcription(request: SummarizationRequest):
    try:
        combined_text = f"{request.transcription}\n\nNotes:\n" + "\n".join(request.notes)
        response = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system",
                 "content": "You are a medical assistant tasked with summarizing patient-doctor conversations and associated notes."},
                {"role": "user",
                 "content": f"""
                 Create a medical transcript summary that preserves the content discussed during the visit and the medical notes by the doctor.\n\n 
                 Provide simple text with concice summary that includes all parts of the visit up to 10 sentences.\n\n 
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

        structured_summary = response.choices[0].message.parsed
        return structured_summary
    except Exception as e:
        logger.error(f"Error summarizing transcription: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/create_documentation", response_model=DocumentationResponse)
async def create_documentation(request: DocumentationRequest):
    try:
        combined_text = "\n\n".join([
            "Transcriptions:",
            *request.transcriptions,
            "Notes:",
            *request.notes,
            "Summaries:",
            *request.summaries
        ])

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
                    3. **Assessment and Plan**: For each condition, begin with the condition name and its corresponding ICD code (if uncertain, provide a list of possible ICD codes). Follow this with a detailed assessment and plan (A&P) for that condition only if such provided in data.\n\n
                    Use only the following information:\n\n
                    {combined_text}.\n\n
                    Do not add any physical exam, result, diagnosis, or assamet and plan information that is not provided explicitly in the input data.
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
