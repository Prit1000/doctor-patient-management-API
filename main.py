from fastapi import FastAPI
import json

app = FastAPI()

def load_patients():
    with open("patients.json", "r") as file:
        data =  json.load(file)
    return data


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


    