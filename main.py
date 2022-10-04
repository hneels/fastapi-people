import json
from turtle import update
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException, status
from models import Person
from typing import Optional
from pydantic import BaseModel
from database import SessionLocal
import models


app = FastAPI()
db = SessionLocal()


# Pydantic serializer
class Person(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True


@app.get("/")
def root():
    return {"hello": "world"}


# greet using path variable
@app.get("/greet/{name}")
def greet(name: str):
    return {"hello": f"{name}"}


# greet using Optional, NO path variable (using query string, like localhost:8000/greet?name=andrew)
@app.get("/greet")
def greet(name: Optional[str] = "fool"):
    return {"hello": f"{name}"}


# get all people in db
@app.get("/people", response_model=list[Person], status_code=200)
def get_all_people():
    # use the db session local instance created
    people = db.query(models.Person).all()
    return people


@app.get("/people/{person_id}")
def get_person(person_id: int):
    person = db.query(models.Person).filter(
        models.Person.id == person_id).first()
    return person


@app.post("/people", response_model=Person, status_code=status.HTTP_201_CREATED)
def create_person(person: Person):

    # create the Person model with data from request body
    new_person = models.Person(
        first_name=person.first_name,
        last_name=person.last_name,
        age=person.age
    )

    # add the new object using session local instance
    db.add(new_person)
    db.commit()

    # return that new person
    return new_person


@app.put("/people/{person_id}", response_model=Person, status_code=status.HTTP_200_OK)
# pass in both the id in the url as well as the Person object in the request body
def update_person(person_id: int, person: Person):
    update_person = db.query(models.Person).filter(
        models.Person.id == person_id).first()
    update_person.first_name = person.first_name
    update_person.last_name = person.last_name
    update_person.age = person.age

    db.commit()
    return update_person


@app.delete("/people/{person_id}")
def delete_person(person_id: int):
    delete_person = db.query(models.Person).filter(
        models.Person.id == person_id).first()

    # throw exception if that person id doesn't exist
    if delete_person is None:
        raise HTTPException(status_code=404, detail="resource not found")

    db.delete(delete_person)
    db.commit()

    # return deleted person
    return delete_person
