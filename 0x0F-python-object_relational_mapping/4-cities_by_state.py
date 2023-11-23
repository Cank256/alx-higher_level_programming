#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def list_cities(username, password, database):
    """List all cities from the database hbtn_0e_4_usa"""
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve all cities with state names,
    # sorted by id
    cursor.execute("\
        SELECT cities.id, cities.name, states.name FROM \
        cities JOIN states ON cities.state_id = states.id ORDER BY \
        cities.id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if all three command-line arguments are provided
    if len(sys.argv) != 4:
        print("Arguments missing")
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list cities
    list_cities(username, password, database)
