#!/usr/bin/python3

def islower(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')
print(islower('a')) #True
print(islower('z')) #True
print(islower('A')) #False
