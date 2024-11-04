from typing import List, Dict, Any, Tuple

from pandera.typing import DataFrame
import pandera as pa
import pandas as pd

from auto_documentation.types import SummaryData, SocialHistory, FamilyHistoryRecord
from auto_documentation.schemas import BaseLabSchema, DiagnosisSchema, DiagnosisEvidenceSchema, FamilyHistorySchema
from auto_documentation.meds.meds import process_medications
from auto_documentation.labs.labs import BaseLab, LoincLab, SupportedBaseLabsNames
from auto_documentation.labs.process import LabProcessingService
from auto_documentation.diagnosis.diagnosis import create_evidence_table, create_diagnoses_table


def process_labs(base_labs, all_labs) -> DataFrame[BaseLabSchema]:
    base_labs = [BaseLab(**lab) for lab in base_labs if SupportedBaseLabsNames.has_value(lab["name"])]
    all_labs = [LoincLab(**lab) for lab in all_labs]
    # Create service
    lab_service = LabProcessingService()

    # Process labs
    return lab_service.process_labs(base_labs, all_labs)


@pa.check_types()
def process_family_history(family_history_data: List[Dict[str, Any]]) -> DataFrame[FamilyHistorySchema]:
    """
    Process family history data into a pandas DataFrame.

    Args:
        family_history_data: List of family history dictionaries

    Returns:
        pd.DataFrame: Processed family history data
    """
    # Convert the list of dictionaries to Pydantic models
    family_history = [FamilyHistoryRecord(**record) for record in family_history_data]
    # convert to DataFrame withe relevant columns
    df = pd.DataFrame([record.dict() for record in family_history])
    return df


def process_diagnoses(suggestions_data) -> Tuple[DataFrame[DiagnosisSchema], DataFrame[DiagnosisEvidenceSchema]]:
    # flatten the list of lists
    input_diagnoses = [d for sublist in suggestions_data for d in sublist]

    diagnoses = create_diagnoses_table(input_diagnoses)
    evidences = create_evidence_table(input_diagnoses)

    return diagnoses, evidences


def process_raw_summary_data(raw_summary_data: Dict[str, Any]) -> SummaryData:
    diagnoses, diagnoses_evidence = process_diagnoses(raw_summary_data["suggestions"])
    print("created diagnoses and evidence tables")
    summary_data = SummaryData(
        diagnoses=diagnoses,
        diagnoses_evidence=diagnoses_evidence,
        medications=process_medications(raw_summary_data["meds"]),
        labs=process_labs(raw_summary_data["base_labs"], raw_summary_data["all_labs"]),
        family_history=process_family_history(raw_summary_data["family_history"]),
        social_history=SocialHistory(**raw_summary_data["social_history"])
    )

    return summary_data
