from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    
    
    contact_details:Dict[str,str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls,model):
        if model.age >60 and "emergency" not in model.contact_details:
            raise ValueError("patients older than 60 must have a emergency contact")
        return model 
    

patient_info = {"name":"keshav","email":"abc@hdfc.com","age":65,
                "contact_details":{"phone_no":"98137546789",'emergency':'235236'}
                }

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
   
    print("inserted")

patient1= Patient(**patient_info)

insert_patient_data(patient1)

## 3_model_validator.py