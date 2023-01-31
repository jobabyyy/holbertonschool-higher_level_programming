#!/usr/bin/python3
"""Base Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """you square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
