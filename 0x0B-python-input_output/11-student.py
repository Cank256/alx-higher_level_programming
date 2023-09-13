#!/usr/bin/python3
"""
A class Student that defines a student by:
(based on 10-student.py)
"""


class Student:
    """
    Defines a student with attributes first_name, last_name, and age.
    Provides methods for JSON representation and deserialization.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names
            to include in the dictionary.
                If None, all attributes will be included.

        Returns:
            dict: A dictionary representation of the student.
        """
        if attrs is None:
            # Include all attributes
            student_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            # Include only specified attributes
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
        return student_dict

    def reload_from_json(self, json_data):
        """
        Replaces all attributes of the Student instance
        with values from a JSON dictionary.

        Args:
            json_data (dict): A dictionary representing the
            attributes and their values.

        Returns:
            None
        """
        for key, value in json_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
