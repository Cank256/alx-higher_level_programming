#!/usr/bin/python3
"""Script that creates the State "California"
with the City "San Francisco"
from the database hbtn_0e_100_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def create_california_san_francisco(username, password, database):
    """Create the State "California" with the City "San Francisco"
    from the database hbtn_0e_100_usa"""
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

    # Create the State "California" and the City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add the State and City objects to the session
    session.add(california)
    session.add(san_francisco)

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

    # Call the function to create California and San Francisco
    create_california_san_francisco(username, password, database)
