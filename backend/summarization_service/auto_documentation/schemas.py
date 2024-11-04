import pandera as pa
from pandera.typing import Series
from pandera.dtypes import DateTime


# Diagnosis related schemas
class DiagnosisSchema(pa.DataFrameModel):
    icdCode: Series[str] = pa.Field()
    icdDescription: Series[str] = pa.Field()
    snomedCode: Series[str] = pa.Field(nullable=True)
    hccGroup: Series[int] = pa.Field(nullable=True)
    hccWeight: Series[float] = pa.Field(nullable=True)
    hccRxWeight: Series[float] = pa.Field(nullable=True)
    hccV24Weight: Series[float] = pa.Field(nullable=True)
    hccV28Weight: Series[float] = pa.Field(nullable=True)
    status: Series[str] = pa.Field(nullable=True)
    isValid: Series[bool] = pa.Field()
    sourceCount: Series[int] = pa.Field()


class DiagnosisEvidenceSchema(pa.DataFrameModel):
    icdCode: Series[str] = pa.Field()
    sourceType: Series[str] = pa.Field()
    sourceName: Series[str] = pa.Field()
    sourceDate: Series[str] = pa.Field()
    hasDocument: Series[bool] = pa.Field()
    documentId: Series[str] = pa.Field(nullable=True)
    documentName: Series[str] = pa.Field(nullable=True)


class MedicationSchema(pa.DataFrameModel):
    name: Series[str] = pa.Field()
    dosage: Series[str] = pa.Field(nullable=True)
    frequency: Series[str] = pa.Field(nullable=True)
    medication_date: Series[DateTime] = pa.Field(nullable=True)
    atc_level2: Series[str] = pa.Field()
    atc_level5: Series[str] = pa.Field()
    rxcui: Series[str] = pa.Field(nullable=True)

    class Config:
        coerce = True


# Pandera Schemas for DataFrame validation
class BaseLabSchema(pa.DataFrameModel):
    name: Series[str] = pa.Field()
    date: Series[DateTime] = pa.Field(nullable=True)
    observationValue: Series[str] = pa.Field(nullable=True)
    category: Series[str] = pa.Field(nullable=True)

    class Config:
        coerce = True
        strict = False


class FamilyHistorySchema(pa.DataFrameModel):
    problem: Series[str] = pa.Field()
    relation: Series[str] = pa.Field()

    class Config:
        coerce = True
