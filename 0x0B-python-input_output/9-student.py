#!/usr/bin/python3
"""
A class Student that defines a student
"""


class Student:
    """
    Defines a student with attributes first_name, last_name, and age.
    Provides a method to retrieve a dictionary representation of the
    student instance.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary representation of the student.
        """
        # Create a dictionary with the student's attributes
        student_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return student_dict
