#!/usr/bin/python3
"""Module that contains the class definition
of State and an instance Base"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    """Class definition of State"""

    # Link to the MySQL table 'states'
    __tablename__ = 'states'

    # Class attribute id that represents a column
    # of an auto-generated, unique integer, can’t be null and is a primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Class attribute name that represents a column
    # of a string with a maximum of 128 characters and can’t be null
    name = Column(String(128), nullable=False)


# Create an engine to connect to the MySQL server
# running on localhost at port 3306
# Replace 'your_username', 'your_password',
# 'your_database' with actual values
engine = create_engine(
    'mysql+mysqldb://your_username:your_password@localhost:3306/your_database'
)

# WARNING: All classes who inherit from Base must be
# imported before calling Base.metadata.create_all(engine)
Base.metadata.create_all(engine)
