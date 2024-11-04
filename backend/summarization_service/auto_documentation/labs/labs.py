from typing import Optional, List, Dict, Tuple, Any
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class SupportedBaseLabsNames(str, Enum):
    HBA1C = "HbA1c"
    EGFR_NAA = "eGFR NAA (raw)"
    KIDNEY_FUNCTION = "Kidney function"
    LIPID_PROFILE = "Lipid profile"
    CBC = "CBC"
    LIVER_FUNCTION = "Liver function"
    THYROID = "Thyroid"
    ELECTROLYTES = "Electrolytes"
    GLUCOSE = "Glucose"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class LabNames(str, Enum):
    HBA1C = "HbA1c"
    DIABETES_STATUS = "Diabetes status"
    HBA1C_TREND = "HbA1c trend"
    CKD_STATUS = "CKD status"
    EGFR_TREND = "eGFR trend"
    EGFR_NAA = "eGFR NAA"
    ALB_CREA = "Alb/Crea ratio (urine)"
    MICROALB = "Microalbumin (urine)"
    TOTAL_CHOLESTEROL = "tc"
    TRIGLYCERIDES = "tg"
    LDL = "ldl"
    HDL = "hdl"
    HGB = "hgb"
    WBC = "wbc"
    PLT = "plt"
    ALT = "alt"
    AST = "ast"
    ALP = "alp"
    BILIRUBIN = "bilirubin (tot)"
    ALBUMIN = "albumin"
    FT4 = "ft4F"
    SODIUM = "sodium"
    POTASSIUM = "potassium"
    CHLORIDE = "chloride"
    GLUCOSE = "glucose"
    BUN = "bun"
    CREATININE = "creatinine"
    TSH = "tsh"
    RBC = "rbc"
    VLDL = "vldl"
    MCV = "mcv"
    NEUTROPHILS = "neutrophils"
    LYMPHOCYTES = "lymphocytes"
    MONOCYTES = "monocytes"
    EOSINOPHILS = "eosinophils"
    BASOPHILS = "basophils"


class LabCategory(str, Enum):
    OTHER = "Other Labs"
    LIPIDS = "Lipid Profile"
    KIDNEY = "Kidney Function"
    LIVER = "Liver Function"
    CBC = "Complete Blood Count"
    THYROID = "Thyroid Function"
    DIABETES = "Diabetes Markers"
    ELECTROLYTES = "Electrolytes"


# Models
class BaseLab(BaseModel):
    name: SupportedBaseLabsNames
    data: Any
    type: Optional[str] = None
    observations: Optional[Any] = None


class LoincLab(BaseModel):
    code: Optional[str] = None
    name: str
    observationName: str
    observationValue: str
    referenceRange: Optional[str] = None
    unit: Optional[str] = None
    resultDate: datetime
    source: Optional[str] = None
    method: Optional[str] = None
    originalResultCode: Optional[str] = None


class CategoryMapping(BaseModel):
    keywords: List[str]
    lab_names: List[LabNames]
    aliases: Dict[str, LabNames] = {}


class LoincMapping:
    def __init__(self):
        # Category mappings for general classification
        self.category_mappings: Dict[LabCategory, CategoryMapping] = {
            LabCategory.LIPIDS: CategoryMapping(
                keywords=['cholesterol', 'triglycerides', 'hdl', 'ldl', 'vldl', 'lipid'],
                lab_names=[
                    LabNames.TOTAL_CHOLESTEROL,
                    LabNames.HDL,
                    LabNames.LDL,
                    LabNames.VLDL,
                    LabNames.TRIGLYCERIDES
                ],
                aliases={
                    'cholesterol, total': LabNames.TOTAL_CHOLESTEROL,
                    'hdl cholesterol': LabNames.HDL,
                    'ldl cholesterol': LabNames.LDL,
                    'vldl cholesterol': LabNames.VLDL,
                }
            ),
            LabCategory.KIDNEY: CategoryMapping(
                keywords=['creatinine', 'egfr', 'albumin', 'microalbumin', 'bun'],
                lab_names=[
                    LabNames.EGFR_NAA,
                    LabNames.ALB_CREA,
                    LabNames.MICROALB,
                    LabNames.BUN,
                    LabNames.CREATININE
                ],
                aliases={
                    'blood urea nitrogen': LabNames.BUN,
                }
            ),
            LabCategory.LIVER: CategoryMapping(
                keywords=['alt', 'ast', 'alkaline phosphate', 'bilirubin', 'albumin', 'sgpt', 'sgot'],
                lab_names=[
                    LabNames.ALT,
                    LabNames.AST,
                    LabNames.ALP,
                    LabNames.BILIRUBIN,
                    LabNames.ALBUMIN
                ],
                aliases={
                    'ast (sgot)': LabNames.AST,
                    'alt (sgpt)': LabNames.ALT,
                    'alkaline phosphate': LabNames.ALP,
                    'bilirubin, total': LabNames.BILIRUBIN,
                }
            ),
            LabCategory.CBC: CategoryMapping(
                keywords=[
                    'hemoglobin', 'platelets', 'wbc', 'rbc', 'hematocrit',
                    'neutrophils', 'lymphocytes', 'monocytes', 'eosinophils',
                    'basophils', 'mcv'
                ],
                lab_names=[
                    LabNames.HGB,
                    LabNames.PLT,
                    LabNames.WBC,
                    LabNames.RBC,
                    LabNames.MCV,
                    LabNames.NEUTROPHILS,
                    LabNames.LYMPHOCYTES,
                    LabNames.MONOCYTES,
                    LabNames.EOSINOPHILS,
                    LabNames.BASOPHILS
                ],
                aliases={
                    'neutrophils (absolute)': LabNames.NEUTROPHILS,
                    'lymphocytes (absolute)': LabNames.LYMPHOCYTES,
                    'monocytes (absolute)': LabNames.MONOCYTES,
                    'eosinophils (absolute)': LabNames.EOSINOPHILS,
                    'basphils (absolute)': LabNames.BASOPHILS,
                    'platelets': LabNames.PLT,
                    'hemoglobin': LabNames.HGB,
                }
            ),
            LabCategory.THYROID: CategoryMapping(
                keywords=['tsh', 'ft4', 'thyroid'],
                lab_names=[LabNames.FT4, LabNames.TSH],
                aliases={
                    'ft4': LabNames.FT4,
                    'tsh': LabNames.TSH,
                }
            ),
            LabCategory.ELECTROLYTES: CategoryMapping(
                keywords=['sodium', 'potassium', 'chloride', 'pottasium'],
                lab_names=[
                    LabNames.SODIUM,
                    LabNames.POTASSIUM,
                    LabNames.CHLORIDE
                ],
                aliases={
                    'pottasium': LabNames.POTASSIUM,
                }
            ),
            LabCategory.DIABETES: CategoryMapping(
                keywords=['glucose', 'hba1c', 'a1c'],
                lab_names=[LabNames.GLUCOSE, LabNames.HBA1C],
                aliases={
                    'Hba1C': LabNames.HBA1C,
                }
            )
        }

    def categorize_lab(self, observation_name: str) -> Tuple[Optional[LabNames], Optional[LabCategory]]:
        """
        Categorize a lab test based on its observation name.
        Returns a tuple of (LabNames or None, LabCategory or None)
        """
        observation_name_lower = observation_name.lower().strip()

        # Check each category
        for category, mapping in self.category_mappings.items():
            # First check aliases for exact matches
            if observation_name_lower in mapping.aliases:
                return mapping.aliases[observation_name_lower], category

            # Then check for keyword matches
            if any(keyword in observation_name_lower for keyword in mapping.keywords):
                # Look for exact matches within lab names
                for lab_name in mapping.lab_names:
                    lab_str = str(lab_name).lower()
                    if lab_str in observation_name_lower or observation_name_lower in lab_str:
                        return lab_name, category

                # Look for common variations
                for alias, lab_name in mapping.aliases.items():
                    if alias in observation_name_lower or observation_name_lower in alias:
                        return lab_name, category

                # If no exact match found, return None for lab_name but still return the category
                return None, category

        # If no matches found, categorize as OTHER
        return None, LabCategory.OTHER

    def get_all_mappings(self) -> Dict[str, Tuple[LabNames, LabCategory]]:
        """
        Returns all known mappings for debugging and verification purposes
        """
        mappings = {}

        # Add category mappings
        for category, mapping in self.category_mappings.items():
            # Add direct lab name mappings
            for lab_name in mapping.lab_names:
                mappings[str(lab_name).lower()] = (lab_name, category)

            # Add aliases
            for alias, lab_name in mapping.aliases.items():
                mappings[alias.lower()] = (lab_name, category)

        return mappings
