from pydantic import BaseModel , AnyUrl , EmailStr , Field ,field_validator
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
    # to check email validation. like employee is from perticular company.
    # now we have to create a method inside the class.
    #use this this with this decorator @field_validator to validate the email field.
    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        
        valid_domains = ["example.com", "test.com"] # list of valid domains
        domain_name = value.split("@")[1] # get the domain name from the email address
        if domain_name not in valid_domains: # check if the domain name is in the list
            raise ValueError(f"Email domain must be one of the following: {', '.join(valid_domains)}") # raise a validation error if the domain name is not valid
        return value # return the email address if it is valid
    
    # to make patient name in uppercase
    @field_validator("name")
    @classmethod
    def name_uppercase(cls,value):
        return value.upper() # return the name in uppercase
    


patient_info = {
    "name": "John Doe",
    "age": 30,
    "weight": 70,
    "married": False,
    "allergies": ["pollen", "dust"],
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
    print(f"Patient Email: {patient.email}")
    print(f"Patient weight: {patient.weight}")
# this function takes a Patient object as an argument and prints the patient's name and age

#now we will call the validate_patient_info function with the patient1 object
validate_patient_info(patient1)


