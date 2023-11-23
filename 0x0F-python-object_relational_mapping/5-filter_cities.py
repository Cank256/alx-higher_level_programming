#!/usr/bin/python3
"""Script that lists all cities of a given state
from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
    """List all cities of a given state from
    the database hbtn_0e_4_usa"""
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

    # Use a parameterized query to avoid SQL injection
    query = "SELECT * FROM cities WHERE state_name = %s ORDER BY id ASC"

    # Execute the SQL query with the parameterized argument
    cursor.execute(query, (state_name,))

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
    if len(sys.argv) != 5:
        print("Arguments missing")
        sys.exit(1)

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to list cities by state
    list_cities_by_state(username, password, database, state_name)
