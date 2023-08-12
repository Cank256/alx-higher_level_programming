#!/usr/bin/python3
from calculator_1 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(a, b):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
