#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('Size must be an integer')
        if size < 0:
            raise ValueError('Size must be greater than zero')
        self.__size = size