#!/usr/bin/python3
"""
A function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8 encoded) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    # Open the file for reading
    with open(filename, "r", encoding="utf-8") as file:
        # Read and print each line in the file
        for line in file:
            print(line, end="")
