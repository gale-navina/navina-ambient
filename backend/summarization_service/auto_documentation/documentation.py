import os
from typing import List, Dict, Hashable, Any
from collections import defaultdict

from fastapi import HTTPException
from openai import OpenAI
from pandera.typing import DataFrame

from auto_documentation.types import SummaryData, ConditionRelevantData, MedsMapping, LabsMapping, ConditionAndLabs, \
    ConditionAndMeds, ConditionAssessment, AssessmentResponse
from auto_documentation.schemas import DiagnosisSchema, MedicationSchema, BaseLabSchema
from auto_documentation.prompts import BATCH_LABS_ASSIGNMENT_PROMPT, BATCH_MEDS_ASSIGNMENT_PROMPT, \
    CONDITION_ASSESSMENT_PROMPT
from auto_documentation.processors import process_raw_summary_data

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def batch_assign_relevant_data(
        conditions: DataFrame[DiagnosisSchema],
        labs_df: DataFrame[BaseLabSchema],
        medications_df: DataFrame[MedicationSchema]
) -> Dict[Hashable, ConditionRelevantData]:
    # Prepare labs and medications strings for prompts
    labs_text = "\n".join([
        f"{i}: {row['name']} | {row['category']} = {row['observationValue']} ({row['date']})"
        for i, row in labs_df.iterrows()
    ])

    meds_text = "\n".join([
        f"{i}: {row['name']} (ATC2: {row['atc_level2']}, ATC5: {row['atc_level5']}, rxcui: {row['rxcui']}) | {row['dosage']} {row['frequency']} ({row['medication_date']})"
        for i, row in medications_df.iterrows()
    ])

    conditions_text = "\n".join([
        f"{i}: {diag['icdDescription']} (ICD: {diag['icdCode']})"
        for i, diag in conditions.iterrows()
    ])

    # Get lab assignments
    labs_response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a medical assistant that identifies relevant labs for conditions."},
            {"role": "user", "content": BATCH_LABS_ASSIGNMENT_PROMPT.format(
                conditions=conditions_text,
                labs=labs_text
            )}
        ],
        response_format=LabsMapping,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0
    )

    lab_structured = labs_response.choices[0].message.parsed

    print(BATCH_MEDS_ASSIGNMENT_PROMPT.format(
        conditions=conditions_text,
        medications=meds_text
    ))

    # Get medication assignments
    meds_response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system",
             "content": "You are a medical assistant that identifies relevant medications for conditions."},
            {"role": "user", "content": BATCH_MEDS_ASSIGNMENT_PROMPT.format(
                conditions=conditions_text,
                medications=meds_text
            )}
        ],
        response_format=MedsMapping,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0
    )
    med_structured = meds_response.choices[0].message.parsed

    print(med_structured)

    # Process responses
    final_mapping = defaultdict(ConditionRelevantData)

    for lab_assignment in lab_structured.labs_mapping:
        lab_assignment: ConditionAndLabs
        final_mapping[lab_assignment.condition_index].relevant_lab_indices = lab_assignment.lab_indices

    for med_assignment in med_structured.meds_mapping:
        med_assignment: ConditionAndMeds
        final_mapping[med_assignment.condition_index].relevant_med_indices = med_assignment.med_indices

    return final_mapping


def assess_conditions(request: SummaryData) -> List[ConditionAssessment]:
    try:
        # First, batch assign relevant labs and medications
        relevant_data = batch_assign_relevant_data(
            request.diagnoses,
            request.labs,
            request.medications
        )

        assessments = []

        for index, diagnosis in request.diagnoses.iterrows():
            # Get relevant data for this condition
            condition_data = relevant_data[index]

            # Prepare data for assessment
            # TODO: Fix this evidences_text = "\n".join([f"- {e.text} ({e.date})" for e in diagnosis.evidences])

            relevant_labs = request.labs.loc[list(condition_data.relevant_lab_indices)]
            labs_text = "\n".join([
                f"- {row['name']} : {row['observationValue']} ({row['date']})"
                for _, row in relevant_labs.iterrows()
            ])

            relevant_meds = request.medications.loc[list(condition_data.relevant_med_indices)]
            meds_text = "\n".join([
                f"- {row['name']} {row['dosage']} {row['frequency']}"
                for _, row in relevant_meds.iterrows()
            ])

            family_history_text = "\n".join([
                f"- {row['problem']} in {row['relation']}"
                for _, row in request.family_history.iterrows()
            ])

            social_history_text = request.social_history.dict() if request.social_history else "No social history provided"

            # Generate assessment
            assessment_response = client.beta.chat.completions.parse(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "system", "content": "You are a medical assistant creating condition assessments."},
                    {"role": "user", "content": CONDITION_ASSESSMENT_PROMPT.format(
                        condition=diagnosis.name,
                        icd_code=diagnosis.icdCode,
                        evidences="",  # TODO: Fix this evidences_text,
                        relevant_labs=labs_text,
                        relevant_meds=meds_text,
                        family_history=family_history_text,
                        social_history=social_history_text
                    )}
                ],
                temperature=0,
                max_tokens=300,
                n=1
            )

            print("got assessment response", assessment_response.choices[0].message.content)

            assessments.append(ConditionAssessment(
                diagnosis=diagnosis.icdDescription,
                icd_code=diagnosis.icdCode,
                assessment=assessment_response.choices[0].message.content
            ))

        return assessments

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def document_raw_summary_request(raw_summary_data: Dict[str, Any]) -> AssessmentResponse:
    print("start document_raw_summary_request")
    summary_data = process_raw_summary_data(raw_summary_data)
    return AssessmentResponse(assessments=assess_conditions(summary_data))
