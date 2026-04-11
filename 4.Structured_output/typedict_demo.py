from typing_extensions import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    "name": "kunal", 
    "age": 23
}

print(new_person)

