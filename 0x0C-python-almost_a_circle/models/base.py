#!/usr/bin/python3
"""Base module."""

import json
import csv
import turtle


class Base:
    """Base class for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class.

        Args:
            id (int, optional): The id for the
            instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation
        of a list of dictionaries.

        Args:
            list_dictionaries (list of dict):
            A list of dictionaries.

        Returns:
            str: JSON string representation of
            the list of dictionaries.
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation
            of list_objs to a file.

        Args:
            list_objs (list of Base instances):
            A list of instances.

        Notes:
            - If list_objs is None, save an empty list.
            - The filename must be: <Class name>.json
            (e.g., Rectangle.json).
            - It uses the static method to_json_string
            to convert the list to JSON.
            - It overwrites the file if it already exists.
        """
        filename = cls.__name__ + ".json"
        json_data = []
        if list_objs:
            json_data = [obj.to_dictionary() for obj in list_objs]

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(json_data))

    @staticmethod
    def from_json_string(json_string):
        """Return a list of objects from a
        JSON string representation.

        Args:
            json_string (str):
            A string representing a list of dictionaries.

        Returns:
            list: List of objects represented by json_string.
        """
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes
            set based on the provided dictionary.

        Args:
            **dictionary: Keyword arguments
            representing attributes.

        Returns:
            Base: An instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square
        else:
            raise TypeError("Unsupported class")

        # Update the dummy instance with the provided dictionary
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file.

        Returns:
            list: List of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        instance_list = []

        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_data = file.read()
                if json_data:
                    json_list = cls.from_json_string(json_data)
                    instance_list = [cls.create(**data) for data in json_list]
        except FileNotFoundError:
            pass

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of
        list_objs to a file.

        Args:
            list_objs (list of Base instances):
            A list of instances.

        Notes:
            - If list_objs is None, save an empty list.
            - The filename must be: <Class name>.csv
            (e.g., Rectangle.csv).
        """
        filename = cls.__name__ + ".csv"
        csv_data = []

        if list_objs:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]

            for obj in list_objs:
                data = obj.to_dictionary()
                csv_data.append(data)

            with open(filename, mode="w", newline="", encoding="utf-8") as fil:
                writer = csv.DictWriter(fil, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(csv_data)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances from a CSV file.

        Returns:
            list: List of instances loaded from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        instance_list = []

        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]

                reader = csv.DictReader(file, fieldnames=fieldnames)
                for row in reader:
                    data = {key: int(value) for key, value in row.items()}
                    instance = cls.create(**data)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass

        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using
        the Turtle graphics module.

        Args:
            list_rectangles (list of Rectangle):
            A list of Rectangle instances.
            list_squares (list of Square):
            A list of Square instances.

        Notes:
            - You must have the Turtle graphics module installed.
            - It opens a window and draws all rectangles and squares.
        """
        screen = turtle.Screen()
        screen.title("Turtle Drawing")
        t = turtle.Turtle()
        t.speed(1)

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        screen.exitonclick()


# Usage example
if __name__ == "__main__":
    import random

    # Create some rectangles and squares
    rectangles = []
    squares = []
    for _ in range(3):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        width = random.randint(20, 100)
        height = random.randint(20, 100)
        size = random.randint(20, 100)

        rectangles.append(Rectangle(width, height, x, y))
        squares.append(Square(size, x, y))

    # Draw them using Turtle
    Base.draw(rectangles, squares)
