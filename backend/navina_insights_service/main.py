from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()


class PatientInsightsRequest(BaseModel):
    patientId: str


class PatientInsightsResponse(BaseModel):
    insights: dict


# Mock patient data
mock_patients = {
    "patient1": {
        "name": "John Doe",
        "age": 45,
        "conditions": ["Hypertension", "Type 2 Diabetes"],
        "allergies": ["Penicillin"],
        "recent_labs": {
            "HbA1c": 7.2,
            "Blood Pressure": "130/85"
        }
    },
    "patient2": {
        "name": "Jane Smith",
        "age": 62,
        "conditions": ["Osteoarthritis", "High Cholesterol"],
        "allergies": ["Sulfa drugs"],
        "recent_labs": {
            "Cholesterol": 210,
            "Vitamin D": 28
        }
    }
}


@app.post("/patient-insights", response_model=PatientInsightsResponse)
async def get_patient_insights(request: PatientInsightsRequest):
    if request.patientId not in mock_patients:
        patient_data = random.choice(list(mock_patients.values()))
    else:
        patient_data = mock_patients[request.patientId]

    return {"insights": patient_data}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8004)