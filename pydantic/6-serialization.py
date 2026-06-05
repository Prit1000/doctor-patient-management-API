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

# export the patient1 object to a file

temp = patient1.model_dump()
# this will convert the patient1 object to a dictionary
print(temp)
print(type(temp))

# for json serialization
temp_json = patient1.model_dump_json()
print(temp_json)
print(type(temp_json))

# to export a perticular field to json
temp_json_name = patient1.model_dump_json(include={"name"})
print(temp_json_name)
print(type(temp_json_name))

#to export more than one field to json
temp_json_name_age = patient1.model_dump_json(include={"name", "age"})
print(temp_json_name_age)
print(type(temp_json_name_age))

#to not export a perticular field to json
temp_json_exclude_name = patient1.model_dump_json(exclude={"name"})
print(temp_json_exclude_name)
print(type(temp_json_exclude_name))

#to not export more than one field to json
temp_json_exclude_name_age = patient1.model_dump_json(exclude={"name", "age"})
print(temp_json_exclude_name_age)  
print(type(temp_json_exclude_name_age))

# to not export zip_code from the address field
temp_json_exclude_zip_code = patient1.model_dump_json(exclude={"address": {"zip_code"}})
print(temp_json_exclude_zip_code)
print(type(temp_json_exclude_zip_code))
