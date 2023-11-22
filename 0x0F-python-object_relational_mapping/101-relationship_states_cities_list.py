#!/usr/bin/python3
"""Script that lists all State objects,
and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_states_cities(username, password, database):
    """List all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa"""
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

    # Query all State objects, and corresponding City objects
    states_cities = session.query(State).order_by(State.id, City.id).all()

    # Display the results
    for state in states_cities:
        print(
            "{}: {}"
            .format(state.name, ", ".join(city.name for city in state.cities))
        )

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

    # Call the function to list states and cities
    list_states_cities(username, password, database)
