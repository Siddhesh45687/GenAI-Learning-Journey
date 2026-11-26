from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    height: float
    weight: float
    Salary: int

candidate_detail: Person = {
    'name': 'Siddhesh',
    'age': 21,
    'height': 170.5,
    'weight': 69.56,
    'Salary': 50000
}

student = Person(**candidate_detail)
print(student)