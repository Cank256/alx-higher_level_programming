#!/usr/bin/python3
"""Script that adds the State object "Louisiana"
to the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_louisiana(username, password, database):
    """Add the State object "Louisiana"
    to the database hbtn_0e_6_usa"""
    # Create an engine to connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, database)
    )

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Create a new State object for Louisiana
    louisiana = State(name="Louisiana")

    # Add the State object to the session
    session.add(louisiana)

    # Commit the session to the database
    session.commit()

    # Print the new states.id
    print(louisiana.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    # Check if all three command-line arguments are provided
    import sys
    if len(sys.argv) != 4:
        print("Arguments missing")
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to add Louisiana to the database
    add_louisiana(username, password, database)
