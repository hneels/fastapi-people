from curses import echo
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from credentials import username, password

# connect sqlalchemy toolkit to postgreSQL driver
engine = create_engine(
    f"postgresql://{username}:{password}@localhost/first_db", echo=True)

Base = declarative_base()

# use this in main to access the database
SessionLocal = sessionmaker(bind=engine)
