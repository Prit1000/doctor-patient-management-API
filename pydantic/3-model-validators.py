from pydantic import BaseModel , AnyUrl , EmailStr , Field ,field_validator , model_validator
from typing import List , Dict , Optional ,Annotated

class Patient(BaseModel):
    name: str 
    age: int 
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_info: Dict[str, str]
    
    #we made a pydantic class to validate
    # if we want to validate more than one field.
    # like , add emargency contact number to 60+ age patients.
    @model_validator(mode="after")
    def add_emergency_contact(cls, model):
        if model.age >= 60 and "emergency_contact" not in model.contact_info:
            raise ValueError("Emergency contact is required for patients aged 60 or above.")
        return model

patient_info = {
    "name": "John Doe",
    "age": 90,
    "weight": 70,
    "married": False,
    "allergies": ["pollen", "dust"],
    "email": "john.doe@example.com",
    "contact_info": {"email": "john.doe@example.com", "phone": "123-456-7890" , "emergency_contact": "987-654-3210" }
}
# this is a dictionary with patient information

#now we will create an instance of the Patient class
# using the patient_info dictionary
patient1 = Patient(**patient_info)
# we use ** to unpack the dictionary and
# pass the values as arguments to the Patient class

# now if we run this code , 1st patient_info will be validated against the Patient class
# if the data is valid, it will create an instance of the Patient class and assign it to patient1
# if the data is invalid, it will raise a validation error  

def validate_patient_info(patient : Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")   
    print(f"Patient Email: {patient.email}")
    print(f"Patient weight: {patient.weight}")
    print(f"Patient Contact: {patient.contact_info}")
# this function takes a Patient object as an argument and prints the patient's name and age

#now we will call the validate_patient_info function with the patient1 object
validate_patient_info(patient1)


