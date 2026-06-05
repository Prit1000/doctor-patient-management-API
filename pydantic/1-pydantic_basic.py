from pydantic import BaseModel , AnyUrl , EmailStr , Field
from typing import List , Dict , Optional ,Annotated

class Patient(BaseModel):
    name: str = Annotated[str, Field(min_length=1, max_length=50, title="Name of the patient",description = "The name of the patient",example = ["John Doe", "Jane Smith"])] # this means that the name field is required and must be a string with a minimum length of 1 and a maximum length of 50
    age: int = Field(gt=0,lt=120) # this means that the age field is required and must be a positive integer less than 120
    linkdin: Optional[AnyUrl] = None # this means that the linkdin field is optional and can be a valid URL or None
    email: Optional[EmailStr] = None # this means that the email field is optional and can be a valid email address or None
    weight: Annotated[float, Field(gt=0, strict=True)] # this means that the weight field is required and must be a positive float
    married: Annotated[bool , Field(default=None)] # this means that the married field is required and must be a boolean value with a default value of None
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)] # this means that the allergies field is optional and can max 5 allegies can be added.
    contact_info: Dict[str, str] = None # first str for key and 2nd str for value.

#we made a pydantic class to validate

patient_info = {
    "name": "John Doe",
    "age": 30,
    "weight": 70,
    "married": False,
    "linkdin": "https://www.linkedin.com/in/johndoe",
    "email": "john.doe@example.com",
    "contact_info": {"email": "john.doe@example.com", "phone": "123-456-7890"}
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
    print(f"Patient allergies: {patient.allergies}")
    print(f"Patient LinkedIn: {patient.linkdin}")
    print(f"Patient Email: {patient.email}")
    print(f"Patient weight: {patient.weight}")
# this function takes a Patient object as an argument and prints the patient's name and age

#now we will call the validate_patient_info function with the patient1 object
validate_patient_info(patient1)


    
