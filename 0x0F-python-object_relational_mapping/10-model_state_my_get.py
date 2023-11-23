#!/usr/bin/python3
"""Script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import text


def print_state_by_name(username, password, database, state_name):
    """Print the State object with the name
    passed as an argument from the database hbtn_0e_6_usa"""
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

    # Query the State object by name
    state = session.query(State).filter_by(name=state_name).first()

    # Display the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Check if all four command-line arguments are provided
    import sys
    if len(sys.argv) != 5:
        print("Arguments missing")
        sys.exit(1)

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to print the state by name
    print_state_by_name(username, password, database, state_name)
