#!/usr/bin/python3
"""
A module for text indentation
"""


def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?', and ':' characters.

    Args:
    text (str): The input text.

    Returns:
    None

    Raises:
    TypeError: If text is not a string.

    Example:
    text_indentation("This is a sentence. Is it? Yes: it is.")
    Output:
    This is a sentence

    Is it

    Yes

    it is
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text based on '.', '?', and ':' and
    # print each part with two new lines
    lines = text.split(".")
    lines = [line.strip() for line in lines if line.strip() != ""]
    for line in lines:
        print(line)
        print()

    # Clear any remaining ':' and '?' characters
    text = text.replace(":", "").replace("?", "")
    lines = text.split(":")
    lines = [line.strip() for line in lines if line.strip() != ""]
    for line in lines:
        print(line)
        print()
