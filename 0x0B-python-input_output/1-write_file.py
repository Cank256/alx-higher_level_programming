#!/usr/bin/python3
"""
A function that writes a string to a text
file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8 encoded)
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    # Open the file for writing (and create it if it doesn't exist)
    with open(filename, "w", encoding="utf-8") as file:
        # Write the text to the file
        num_characters_written = file.write(text)

    return num_characters_written
