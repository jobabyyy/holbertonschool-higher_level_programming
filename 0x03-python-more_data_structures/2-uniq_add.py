#!/usr/bin/python3
def uniq_add(my_list=[]):
    # convert list to set to remove duplicate elements
    my_list = set(my_list)
    # filter out any non-integer element
    my_list = filter(lambda x: isinstance(x, int), my_list)
    # return the sum
    return sum(my_list)
