#!/usr/bin/python3
"""OBJ TXT"""
import json


def save_to_json_file(my_obj, filename):
    """SAVE JASON"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
