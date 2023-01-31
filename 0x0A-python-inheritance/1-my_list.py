#!/usr/bin/python3
"""Print sorted and myList"""


class MyList(list):
    """this class contains list"""
    def print_sorted(self):
        """print and sort a list"""
        print(sorted(self))
