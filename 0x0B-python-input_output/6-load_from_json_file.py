#!/usr/bin/python3
"""JSON FILE"""
import json


def load_from_json_file(filename):
    """with statements"""
    with open(filename, 'r') as file:
        return json.load(file)
