#!/usr/bin/python3
"""encoding"""


def read_file(filename=""):
    """comment"""
    with open(filename, 'r', encoding='utf8') as file:
        print(file.read(), end='')
