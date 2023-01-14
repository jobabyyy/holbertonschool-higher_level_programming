#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list): #value of idx is being checked
        return my_list #no changes made, output to be same
    else:
        my_list[idx] = element
        return my_list
