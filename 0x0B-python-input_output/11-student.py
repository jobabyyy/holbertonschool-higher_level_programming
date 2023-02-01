#!/usr/bin/python3
"""pub method"""


class Student:
    """load from json file"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        obj_dict = {
            attr: getattr(self, attr)
            for attr in dir(self) if not callable(getattr(self, attr))
            and not attr.startswith("__") and (attrs is None or attr in attrs)
        }
        return obj_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
