#!/usr/bin/python3
"""who are you???"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        obj_dict = {}
        for attr in dir(self):
            if not callable(getattr(self, attr)) and not attr.startswith("__"):
                obj_dict[attr] = getattr(self, attr)
        return obj_dict
