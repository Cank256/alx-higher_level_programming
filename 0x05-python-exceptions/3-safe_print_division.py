#!/usr/bin/python3
def safe_print_division(a, b):
    result = None  # Initialize result with a default value
    try:
        result = a / b
    except ZeroDivisionError:
        pass  # You can leave it as None
    finally:
        try:
            print("Inside result: {}".format(result))
        except NameError:
            print("Inside result: None")
    
    if result is not None:
        return result
    else:
        return None
