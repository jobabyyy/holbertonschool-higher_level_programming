#!/usr/bin/python3
"""stringing"""


def write_file(filename="", text=""):
    """return num of chars"""
    with open(filename, 'w', encoding='utf8') as file:
        file.write(text)
    return len(text)
