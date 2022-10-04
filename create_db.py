# run once to create the database table from the Person model
from database import Base, engine
from models import Person

print("creating database...")

Base.metadata.create_all(engine)
