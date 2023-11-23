#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Take 3 arguments: mysql username, mysql password, and database name
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Connect to a MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create the State “California” with the City “San Francisco”
    california = State(name="California", cities=[City(name="San Francisco")])

    # Add the State and City to the session
    session.add(california)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
