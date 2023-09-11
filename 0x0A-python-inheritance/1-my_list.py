#!/usr/bin/python3
class MyList(list):
    """
    MyList is a custom class that inherits from the built-in
    list class. It adds a method to print the list in ascending
    sorted order. This class assumes that all elements in the
    list are of type int.

    Attributes:
        Inherits all attributes and methods from the list class.

    Methods:
        print_sorted(self):
            Prints the elements of the list in ascending sorted order.

    Example usage:
        my_list = MyList([3, 1, 2, 5, 4])
        my_list.print_sorted()  # Output: [1, 2, 3, 4, 5]
    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending sorted order.

        Returns:
            None

        Example:
            my_list = MyList([3, 1, 2, 5, 4])
            my_list.print_sorted()  # Output: [1, 2, 3, 4, 5]
        """
        sorted_list = sorted(self)
        print(sorted_list)
