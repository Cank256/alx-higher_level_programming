#!/usr/bin/python3
"""
Module that contains the class definition
of State and an instance Base
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    """
    Class definition of State
    """

    # Link to the MySQL table 'states'
    __tablename__ = 'states'

    # Class attribute id that represents a column
    # of an auto-generated, unique integer, can’t be null and is a primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Class attribute name that represents a column
    # of a string with a maximum of 128 characters and can’t be null
    name = Column(String(128), nullable=False)

    # Relationship to the City class
    cities = relationship(
        "City", back_populates="state", cascade="all, delete-orphan"
    )
