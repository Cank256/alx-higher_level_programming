#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # for value in a_dictionary:
    #     value * 2
    # return a_dictionary
    return {key: value * 2 for key, value in a_dictionary.items()}
