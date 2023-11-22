#!/usr/bin/python3
"""
Script that displays all values in the states table
where name matches the argument
"""

import MySQLdb
import sys


def search_states_by_name(username, password, database, state_name):
    """
    Display all values in the states table
    where name matches the argument
    """
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

    # Use format to create the SQL query with the user input
    query_text = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    query = query_text.format(state_name)

    # Execute the SQL query
    cursor.execute(query)

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
    username, password, database, state_name = sys.argv[1],
    sys.argv[2], sys.argv[3], sys.argv[4]

    # Call the function to search states by name
    search_states_by_name(username, password, database, state_name)
