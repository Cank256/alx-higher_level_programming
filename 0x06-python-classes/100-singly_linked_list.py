#!/usr/bin/python3
"""
Singly Linked List
"""


class Node:
    """
    A class representing a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list.
                                       Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If the provided data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If the provided next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head: The first node in the linked list.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the
        linked list.
        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data <= value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def display(self):
        """
        Prints the entire linked list.
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next_node
