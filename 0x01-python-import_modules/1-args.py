#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # remove the first element, which is the script name
    argc = len(argv)
    if argc == 1:
        print(f"{argc} argument:")
    else:
        print(f"{argc} arguments:")
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
    if argc == 0:
        print(".")
    else:
        print("")
