from pydantic import BaseModel
from typing import List , Dict , Optional 

class Adress(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str 
    age: int
    gender: str
    address: Adress
    
address_info = {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip_code": "12345"
}
address1 = Adress(**address_info) # we can also create an instance of the Adress class using the address_info dictionary

patient_info = {
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "address": address1
}
patient1 = Patient(**patient_info)   

print(patient1)
print(patient1.name)
print(patient1.address)
print(patient1.address.city)
print(patient1.address.zip_code)