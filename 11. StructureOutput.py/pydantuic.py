from pydantic import EmailStr,BaseModel,Field
from typing import Optional

class person(BaseModel):
    name:str ='Siddhesh'
    age:Optional[int] = None
    Email:EmailStr
    cgpa: float = Field(gt=0 , lt=10, default=5, description='A decimal value representing the cgpa of the student')

new_student = {'age':20,'Email':'siddhesh@gmail.com','cgpa':9.26}

student = person(**new_student)
student_list = list(student)
student_json = student.model_dump_json()

print(student_list)
print(student_json)