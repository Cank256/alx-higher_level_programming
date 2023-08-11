#!/usr/bin/python3
from add_0 import add


def addition(a, b):
    result = add(a, b)

    print("{} + {} = {}".format(a, b, result))


addition(1, 2)
