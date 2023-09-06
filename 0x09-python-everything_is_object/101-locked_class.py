#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")

# Example usage:
obj = LockedClass()
obj.first_name = "John"  # This is allowed
print(obj.first_name)    # Output: John

# Trying to set another attribute will raise an AttributeError
obj.last_name = "Doe"    # This will raise an AttributeError
