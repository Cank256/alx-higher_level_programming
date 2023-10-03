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
        """Setter for the size attribute,
        assigns to width and height.

        Args:
            value (int): The new size value.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the
        Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign attributes using both *args and **kwargs.

        Args:
            *args: List of arguments in the
            order (id, size, x, y).
            **kwargs: Keyword arguments representing
            attribute assignments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
