from fastapi import FastAPI , Path , HTTPException , Query
from pydantic import BaseModel , Field , computed_field
from fastapi.responses import JSONResponse
from typing import Annotated , Literal ,Optional
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(...,description="Unique identifier for the patient", example="P001")]
    name: Annotated[str,Field(...,description="Name of the patient", example="John Doe")]
    city: Annotated[str, Field(...,description="City of the patient", example="New York")]
    age: Annotated[int,Field(...,gt=0,lt=120,description="Age of the patient", example=30)]
    gender: Annotated[Literal["Male", "Female", "Other"], Field(...,description="Gender of the patient", example="Male")]
    height: Annotated[float, Field(...,gt=0,description="Height of the patient in m", example=1.755)]
    weight: Annotated[float, Field(...,gt=0,description="Weight of the patient in kg", example=70.0)]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi =  round(self.weight / (self.height ** 2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        bmi = self.bmi
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

class patient_update(BaseModel):
    name: Annotated[Optional[str], Field(default=None,description="Name of the patient", example="John Doe")]
    city: Annotated[Optional[str], Field(default=None,description="City of the patient", example="New York")]
    age: Annotated[Optional[int],Field(default=None,gt=0,lt=120,description="Age of the patient", example=30)]
    gender: Annotated[Optional[Literal["Male", "Female", "Other"]], Field(default=None,description="Gender of the patient", example="Male")]
    height: Annotated[Optional[float], Field(default=None,gt=0,description="Height of the patient in m", example=1.755)]
    weight: Annotated[Optional[float], Field(default=None,gt=0,description="Weight of the patient in kg", example=70.0)]
    
    
def load_patients():
    with open("patients.json", "r") as file:
        data =  json.load(file)
    return data

def save_patients(patients):
    with open("patients.json", "w") as file:
        json.dump(patients, file, indent=4)
    # this function will save the patients data to patients.json file in a formatted way with indent of 4 spaces.

@app.get("/")
def read_root():
    return {"message": "Welcome to the Doctor-Patient management API!"}

@app.get("/about")
def about():
    return {"message": "This API allows you to manage doctor and patient information."}

@app.get("/view")
def view_patients():
    patients = load_patients()
    return patients

@app.get("/view/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="P001")):
    patients = load_patients()
    if patient_id in patients:
        return patients[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort_patients(sort_by: str = Query(...,description = "sort on the basis of height, weight, bmi"),order: str = Query("asc", description="Sort order: 'asc' for ascending, 'desc' for descending")):
    valid_fields = ["height", "weight", "bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid options are: {valid_fields}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order. Valid options are: 'asc' or 'desc'")
    patients = load_patients()
    
    sort_order = True if order == "desc" else False
    sorted_patients = sorted(patients.items(), key=lambda x: x[1][sort_by], reverse=sort_order)
    return sorted_patients
    

@app.post("/create")
def create_patient(patient: Patient):
    # patient data will be comming from client which follow Patient data type.
    #now patient have all data sending from client and also have computed field bmi and verdict.
    patients = load_patients()
    # check if patient with same id already exist or not if exist then raise error otherwise add patient to patients.json file.
    if patient.id in patients:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    # first convert this pydantic data (patient) to dictionary using dict() method and then add this patient to patients dictionary with patient id as key and patient data as value.
    patients[patient.id] = patient.model_dump(exclude=["id"])
    save_patients(patients)
    return JSONResponse(status_code=201,content={"message": "Patient created successfully"})


@app.put("/edit/{patient_id}")
def edit_patient(patient_id: str = Path(..., description="The ID of the patient to update", example="P001"), patient_update: patient_update = None):
    patients = load_patients()
    if patient_id not in patients:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    patient_data = patients[patient_id]
    update_data = patient_update.model_dump(exclude_unset=True) 
    # this will give us only the fields which are sent by client for update and exclude the fields which are not sent by client.
    
    for key, value in update_data.items():
        patient_data[key] = value
    
    # patient_data -> pydantic object -> we need to convert this patient_data to Patient object to get the computed fields bmi and verdict updated according to the new height and weight. -> then convert this updated Patient object back to dictionary and save it to patients.json file.
    
    patient_data["id"] = patient_id
    updated_patient = Patient(**patient_data)
    updated_patient_dict = updated_patient.model_dump(exclude=["id"])
    
    patients[patient_id] = updated_patient_dict
    save_patients(patients)

    return JSONResponse(status_code=200, content={"message": "Patient updated successfully"})   


@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str = Path(..., description="The ID of the patient to delete", example="P001")):
    patients = load_patients()
    if patient_id not in patients:
        raise HTTPException(status_code=404, detail="Patient not found")
    del patients[patient_id]
    save_patients(patients)
    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})



    
    
    