#!/usr/bin/python3

def uppercase(string):
    for char in string:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            print(chr(ord(char) - ord('a') + ord('A')), end='')
        else:
            print(char, end='')
    print()
