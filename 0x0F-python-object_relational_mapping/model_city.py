#!/usr/bin/python3
"""Module that contains the class definition
of City and an instance Base"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Class definition of City"""

    # Link to the MySQL table 'cities'
    __tablename__ = 'cities'

    # Class attribute id that represents a column
    # of an auto-generated, unique integer, can’t be null and is a primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Class attribute name that represents a column
    # of a string with a maximum of 128 characters and can’t be null
    name = Column(String(128), nullable=False)

    # Class attribute state_id that represents a column
    # of an integer, can’t be null and is a foreign key to states.id
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Relationship to the State class
    state = relationship("State", back_populates="cities")
