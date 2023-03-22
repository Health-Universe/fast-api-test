from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PatientData(BaseModel):
    weight: float
    glucose_level: float
    insulin_sensitivity_factor: float

@app.post("/calculate")
async def calculate_basal_insulin_dose(patient_data: PatientData):
    basal_insulin_dose = patient_data.weight / patient_data.insulin_sensitivity_factor
    return {"basal_insulin_dose": basal_insulin_dose}

@app.get("/about")
async def about():
    return {"about":"This is a sample application"}
