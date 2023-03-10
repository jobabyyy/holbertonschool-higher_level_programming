#!/usr/bin/python3
"""import from json"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """comment"""
    try:
        load_this = load_from_json_file("add_item.json")
    except FileNotFoundError:
        load_this = []
    load_this.extend(sys.argv[1:])
    save_to_json_file(load_this, "add_item.json")
