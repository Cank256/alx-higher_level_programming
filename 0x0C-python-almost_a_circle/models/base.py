#!/usr/bin/python3
"""
    Base class for managing unique identifiers for objects.

    This class is designed to be the base for other classes
    in the project to manage the 'id' attribute. It ensures that each
    object created from derived classes has a unique 'id' by either
    accepting a provided 'id' or generating one based on an internal counter.

    Attributes:
        __nb_objects (int): A private class attribute to keep track
        of the number of objects created.

    Methods:
        __init__(self, id=None):
            Constructor for the Base class.

            Args:
                id (int, optional): An integer identifier. If provided, it sets
                                    the 'id' attribute to this value. If not
                                    provided, it increments the internal
                                    counter and assigns the new value as the
                                    'id' attribute.

    Examples:
        >>> obj1 = Base()
        >>> obj1.id
        1

        >>> obj2 = Base()
        >>> obj2.id
        2

        >>> obj3 = Base(100)
        >>> obj3.id
        100
"""


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int, optional): An integer identifier. If provided,
                                it sets the 'id' attribute to this value.
                                If not provided, it increments the internal
                                counter and assigns the new value as the
                                'id' attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
