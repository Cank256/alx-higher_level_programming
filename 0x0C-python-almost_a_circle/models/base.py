#!/usr/bin/python3
"""Base module."""


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """Initialize the Base class.

        Args:
            id (int): The id for the Base instance.
            If not provided, it will be auto-generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
