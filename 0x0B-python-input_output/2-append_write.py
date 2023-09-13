#!/usr/bin/python3
"""
A function that appends a string at the end of a
text file (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8 encoded)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    # Open the file for appending (and create it if it doesn't exist)
    with open(filename, "a", encoding="utf-8") as file:
        # Write the text to the file
        num_characters_added = file.write(text)

    return num_characters_added
