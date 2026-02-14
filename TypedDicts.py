from typing import TypedDict

# defining dictionry
class Person(TypedDict):
    name : str
    age :int

# creating new dict of type Person
new_Person:Person ={'name':"Hari",'age':"24"}
print(type(new_Person['age']))

