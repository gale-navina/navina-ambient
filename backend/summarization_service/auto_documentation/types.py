from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List, Set
from pandera.typing import DataFrame

from auto_documentation.schemas import DiagnosisSchema, DiagnosisEvidenceSchema, MedicationSchema, BaseLabSchema, \
    FamilyHistorySchema


class SocialHistory(BaseModel):
    alcoholScreening: Optional[bool]
    isSmoker: Optional[bool]
    isFormerSmoker: Optional[bool]
    numberOfChildren: Optional[int]

    class Config:
        from_attributes = True


class FamilyRelation(str, Enum):
    PATERNAL_AUNT = "Paternal Aunt"
    MATERNAL_GRANDFATHER = "Maternal Grandfather"
    FATHER = "Father"
    MOTHER = "Mother"
    MATERNAL_UNCLE = "Maternal Uncle"
    SIBLING = "Sibling"
    PATERNAL_UNCLE = "Paternal Uncle"
    PATERNAL_GRANDFATHER = "Paternal Grandfather"
    MATERNAL_AUNT = "Maternal Aunt"
    CHILD = "Child"
    GRANDCHILD = "Grandchild"
    GRANDPARENT = "Grandparent"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class FamilyHistoryRecord(BaseModel):
    problem: str
    relation: FamilyRelation

    class Config:
        from_attributes = True


# Input Models
class SummaryData(BaseModel):
    diagnoses: DataFrame[DiagnosisSchema]
    diagnoses_evidence: DataFrame[DiagnosisEvidenceSchema]
    medications: DataFrame[MedicationSchema]
    labs: DataFrame[BaseLabSchema]
    family_history: DataFrame[FamilyHistorySchema]
    social_history: Optional[SocialHistory]


# Output Models

class ConditionAndLabs(BaseModel):
    condition_index: int = Field(..., description="Index of the condition in the input DataFrame")
    lab_indices: List[int] = Field(...,
                                   description="List of indices of labs relevant to the condition, can be empty")


class LabsMapping(BaseModel):
    labs_mapping: List[ConditionAndLabs] = Field(...,
                                                 description="List of mappings between conditions and relevant labs if any")


class ConditionAndMeds(BaseModel):
    condition_index: int = Field(..., description="Index of the condition in the input DataFrame")
    med_indices: List[int] = Field(...,
                                   description="List of indices of medications relevant to the condition, can be empty")


class MedsMapping(BaseModel):
    meds_mapping: List[ConditionAndMeds] = Field(...,
                                                 description="List of mappings between conditions and relevant medications if any")


class ConditionRelevantData(BaseModel):
    relevant_lab_indices: Set[int] = Field(default_factory=set)
    relevant_med_indices: Set[int] = Field(default_factory=set)


class ConditionAssessment(BaseModel):
    diagnosis: str
    icd_code: str
    assessment: str = Field(..., description="Brief medical assessment of the condition based on available evidence")


class AssessmentResponse(BaseModel):
    assessments: List[ConditionAssessment]
