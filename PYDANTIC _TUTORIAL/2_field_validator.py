from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
   
    

    @field_validator("email")
    @classmethod
    def email_validator(cls,value):

        valid_domains= ["hdfc.com","icic.com"]
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value 
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
   
    print("inserted")


patient_info = {"name":"keshav","email":"abc@hdfc.com","age":30,"weight":56,"Linkedin_Url":"https://www.linkedin.com/feed/",
                }

patient1= Patient(**patient_info)

insert_patient_data(patient1)

## 2_field_validator.py