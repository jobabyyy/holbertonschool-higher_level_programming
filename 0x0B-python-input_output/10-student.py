#!/usr/bin/python3
"""JSON W/FILTER"""


class Student:
    """def init"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        obj_dict = {}
        if attrs is None:
            for attr in dir(self):
                if not callable(getattr(self, attr)) and not attr.startswith("__"):
                    obj_dict[attr] = getattr(self, attr)
        else:
            for attr in attrs:
                if hasattr(self, attr):
                    obj_dict[attr] = getattr(self, attr)
        return obj_dict
