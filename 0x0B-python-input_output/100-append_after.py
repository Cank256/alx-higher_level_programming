#!/usr/bin/python3
"""
A function to append text
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a
    specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each
        line containing the search string.

    Returns:
        None
    """
    # Open the file for reading and writing
    with open(filename, "r+") as file:
        lines = file.readlines()
        file.seek(0)  # Reset the file pointer to the beginning

        for line in lines:
            file.write(line)  # Write the original line
            if search_string in line:
                file.write(new_string + '\n')

    # Truncate the file to remove any extra lines
    with open(filename, "r+") as file:
        file.truncate()
