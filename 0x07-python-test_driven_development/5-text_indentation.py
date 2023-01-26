#!/usr/bin/python3
"""doc test"""


def text_indentation(text):
    """indent happen"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    tokens = text.split("\n")
    tokens = [token.strip() for token in tokens]
    text = "\n".join(tokens)
    print(text, end="")
