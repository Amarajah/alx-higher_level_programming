#!/usr/bin/python3

class LockedClass:

    def __init__(self, first_name=""):
        self.first_name = first_name

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError
            ("'LockedClass' object has no attribute {}".format(name))
        object.__setattr__(self, name, value)
