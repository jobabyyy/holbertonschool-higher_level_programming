#!/usr/bin/python3
"""CLASS OBJECT"""


def class_to_json(obj):
    """comment"""
    obj_dict = {}
    for attr in dir(obj):
        if not callable(getattr(obj, attr)) and not attr.startswith("__"):
            obj_dict[attr] = getattr(obj, attr)
    return obj_dict
