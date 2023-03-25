from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://hub.healthuniverse.com",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataModel(BaseModel):
    weight: float

@app.post("/interface")
async def calculate_basal_insulin_dose(patient_data: DataModel):
    tdd = patient_data.weight / 4
    basal = tdd / 2
    return {"basal_insulin_dose": basal}

@app.get("/about")
async def about():
    return {
      "schema_version": "v1",
      "name": "Basal Insulin Dose.",
      "description": "Model for calculating a patients basal insulin dose. Requires weight in lbs.",
      "auth": {
        "type": "none"
      },
      "api": {
        "type": "openapi",
        "is_user_authenticated": false
      },
      "contact_email": "example@healthuniverse.com",
    }
