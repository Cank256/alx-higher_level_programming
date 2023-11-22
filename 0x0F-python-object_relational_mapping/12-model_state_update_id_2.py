#!/usr/bin/python3
"""Script that changes the name of a State
object in the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def change_state_name(username, password, database):
    """Change the name of a State object
    in the database hbtn_0e_6_usa"""
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

    # Query the State object with id = 2
    state_to_change = session.query(State).filter_by(id=2).first()

    # Check if the State object with id = 2 exists
    if state_to_change:
        # Change the name to "New Mexico"
        state_to_change.name = "New Mexico"

        # Commit the session to the database
        session.commit()

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

    # Call the function to change the state name
    change_state_name(username, password, database)
