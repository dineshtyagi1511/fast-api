from pydantic import BaseModel ,EmailStr ,AnyUrl,Field
from typing import List ,Dict,Optional,Annotated

class Patient(BaseModel):
    name :Annotated[str,Field(max_length=50,title ="name of the patient",description="give the name of the patient in less than 50 characters ",examples=["keshav","Dinesh"])]
    email:EmailStr
    Linkedin_Url :AnyUrl
    age:int 
    weight:Annotated[float ,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None,description="is the patient married or not ")]
    allergies: Annotated[Optional[List[str]] , Field(default=None,max_length=5)]
    contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.Linkedin_Url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print("inserted")

patient_info = {"name":"keshav","email":"abc@gmail.com","age":30,"weight":56,"Linkedin_Url":"https://www.linkedin.com/feed/",
                "contact_details":{"phone_no":"98137546789"}}

patient1= Patient(**patient_info)

insert_patient_data(patient1)

##1_pydantic_why.py 



