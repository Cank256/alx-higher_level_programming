#!/usr/bin/python3
"""Square module."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square class.

        Args:
            size (int): The size of the square (both width and height).
            x (int, optional): The x-coordinate of the
            square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the
            square's position. Defaults to 0.
            id (int, optional): The id for the Square
            instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the
        Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Return a dictionary representation
        of the Square instance."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
