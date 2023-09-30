#!/usr/bin/python3
"""
A modules that prints a string

"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name with the provided first name and last name.

    Args:
    first_name (str): The first name.
    last_name (str, optional): The last name. Defaults to an empty string.

    Returns:
    None

    Raises:
    TypeError: If first_name or last_name is not a string.

    Example:
    say_my_name("John", "Doe")  # Output: "My name is John Doe"
    say_my_name("Alice")  # Output: "My name is Alice "
    """
    if not isinstance(first_name, str):
        raise TypeError(
            "first_name must be a string"
        )

    if not isinstance(last_name, str):
        raise TypeError(
            "last_name must be a string"
        )

    full_name = f"My name is {first_name} {last_name}"\
        if last_name else f"My name is {first_name} "
    print(full_name)
