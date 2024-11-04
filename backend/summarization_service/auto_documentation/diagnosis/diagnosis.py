from typing import List, Optional, Dict, Union
from datetime import datetime

from pydantic import BaseModel, Field
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame

from auto_documentation.schemas import DiagnosisSchema, DiagnosisEvidenceSchema


# Pydantic Models (unchanged)
class HccInfo(BaseModel):
    group: Union[str, int]
    weight: float


class HccCategories(BaseModel):
    rx: Optional[List[HccInfo]] = []
    v24: Optional[List[HccInfo]] = []
    v28: Optional[List[HccInfo]] = []


class DiagnosisSource(BaseModel):
    type: str
    date: str
    sourceName: str
    data: List[Dict] = []
    document: Optional[Dict] = None
    extraData: Optional[List[Dict]] = None

    class Config:
        allow_population_by_field_name = True


class Diagnosis(BaseModel):
    icdCode: str
    icdDescription: Optional[str] = None
    snomedCode: Optional[str] = None
    hccs: Optional[HccCategories] = None
    suggestionDate: Optional[datetime] = Field(None, alias="suggestionDateTime")
    diagnosisSources: List[DiagnosisSource]
    reasons: Dict[str, List] = {}
    status: Optional[str] = None
    isValid: Optional[bool] = None
    hccGroup: Optional[int] = None
    hccWeight: Optional[float] = None

    class Config:
        allow_population_by_field_name = True


@pa.check_types()
def create_diagnoses_table(diagnoses: List[Dict]) -> DataFrame[DiagnosisSchema]:
    """
    Create a validated tabular representation of diagnoses metadata.
    """
    relevant_fields = ['icdCode', 'icdDescription', 'snomedCode', 'hccGroup', 'hccWeight', 'hccs', 'suggestionDateTime',
                       'diagnosisSources', 'reasons', 'status', 'isValid']
    diagnoses = [Diagnosis(**{k: d[k] for k in relevant_fields}) for d in diagnoses]
    rows = []
    for dx in diagnoses:
        # Get HCC weights for different models
        hcc_rx = next((h.weight for h in dx.hccs.rx), None) if dx.hccs.rx else None
        hcc_v24 = next((h.weight for h in dx.hccs.v24), None) if dx.hccs.v24 else None
        hcc_v28 = next((h.weight for h in dx.hccs.v28), None) if dx.hccs.v28 else None

        row = {
            'icdCode': dx.icdCode,
            'icdDescription': dx.icdDescription,
            'snomedCode': dx.snomedCode,
            'hccGroup': dx.hccGroup,
            'hccWeight': dx.hccWeight,
            'hccRxWeight': hcc_rx,
            'hccV24Weight': hcc_v24,
            'hccV28Weight': hcc_v28,
            'status': dx.status,
            'isValid': dx.isValid,
            'sourceCount': len(dx.diagnosisSources)
        }
        rows.append(row)

    return pd.DataFrame(rows)


@pa.check_types()
def create_evidence_table(diagnoses: List[Dict]) -> DataFrame[DiagnosisEvidenceSchema]:
    """
    Create a validated tabular representation of diagnosis evidence.
    """
    relevant_fields = ['icdCode', 'diagnosisSources']
    print(diagnoses[0].keys())
    diagnoses = [Diagnosis(**{k: d[k] for k in relevant_fields}) for d in diagnoses]
    rows = []
    for dx in diagnoses:
        for source in dx.diagnosisSources:
            row = {
                'icdCode': dx.icdCode,
                'sourceType': source.type,
                'sourceName': source.sourceName,
                'sourceDate': source.date,
                'hasDocument': bool(source.document),
                'documentId': source.document.get('id') if source.document else None,
                'documentName': source.document.get('name') if source.document else None
            }
            rows.append(row)

    return pd.DataFrame(rows)
