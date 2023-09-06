#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )
