#!/usr/bin/env python3

for i in range(9):
    for j in range(i+1, 10):
        print("{:d}{:d}, ".format(i, j), end='')
print()