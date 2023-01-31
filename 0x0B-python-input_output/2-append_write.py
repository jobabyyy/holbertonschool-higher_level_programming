#!/usr/bin/python3
"""APPEND"""


def append_write(filename="", text=""):
    """func to append string"""
    with open(filename, 'a', encoding='utf8') as file:
        file.write(text)
    return len(text)
