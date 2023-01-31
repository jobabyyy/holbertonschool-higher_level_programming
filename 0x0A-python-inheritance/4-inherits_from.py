#!/usr/bin/python3
"""inherently boring"""


def inherits_from(obj, a_class):
    """you already know who this is"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
