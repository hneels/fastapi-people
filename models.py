from typing import Optional
from uuid import UUID, uuid4
from database import Base
from sqlalchemy import String, Integer, Column


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)

    # return string represeentation of this model
    def __repr__(self):
        return f"{self.first_name} {self.last_name} age: {self.age}"

