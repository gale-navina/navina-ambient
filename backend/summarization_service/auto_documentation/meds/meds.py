from typing import List, Dict, Optional
from datetime import datetime

from pydantic import BaseModel
import pandas as pd
import pandera as pa
from pandera.typing import Series, DataFrame

from auto_documentation.schemas import MedicationSchema


# Pydantic Models
class Medication(BaseModel):
    name: str
    dosage: Optional[str]
    frequency: Optional[str]
    medicationDate: Optional[datetime]
    atcLevel2: List[str]
    atcLevel5: List[str]
    rxcui: List[str]

    class Config:
        from_attributes = True


@pa.check_types()
def process_medications(medications_data: List[Dict]) -> DataFrame[MedicationSchema]:
    """
    Process medication data into a validated pandas DataFrame with expanded ATC codes.

    Args:
        medications_data: List of medication dictionaries containing medication information

    Returns:
        DataFrame[MedicationSchema]: Validated DataFrame containing processed medication data
    """
    # Define relevant fields to extract from input data
    relevant_fields = ['name', 'dosage', 'frequency', 'medicationDate',
                       'atcLevel2', 'atcLevel5', 'rxcui']

    # Filter data and convert to Pydantic models
    filtered_data = [{k: d[k] for k in relevant_fields} for d in medications_data]
    medications = [Medication(**med) for med in filtered_data]

    # Create rows for each ATC code combination
    rows = []
    for med in medications:
        # Create base row with non-ATC fields
        base_row = {
            'name': med.name,
            'dosage': med.dosage,
            'frequency': med.frequency,
            'medication_date': med.medicationDate,
            'rxcui': med.rxcui[0] if med.rxcui else None
        }

        # Create a row for each ATC level2/level5 combination
        for atc2, atc5 in zip(med.atcLevel2, med.atcLevel5):
            row = base_row.copy()
            row['atc_level2'] = atc2
            row['atc_level5'] = atc5
            rows.append(row)

    # Convert to DataFrame
    df = pd.DataFrame(rows)

    # Sort by medication date and name
    df = df.sort_values(['medication_date', 'name'])

    # Reorder columns for better readability
    column_order = [
        'name', 'dosage', 'frequency',
        'medication_date', 'atc_level2', 'atc_level5', 'rxcui'
    ]

    return df[column_order]
