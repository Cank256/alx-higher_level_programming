#!/usr/bin/python3
"""
A script that adds all arguments to a Python list,
and then save them to a file:
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Get the command-line arguments, excluding the script name
arguments = sys.argv[1:]

# Load existing data or initialize an empty list
try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []

# Append the new arguments to the existing list
data.extend(arguments)

# Save the updated list back to the file
save_to_json_file(data, "add_item.json")
