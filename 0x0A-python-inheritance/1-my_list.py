#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        print(sorted(self))

my_list = MyList([3, 2, 1])
my_list.print_sorted() # prints [1, 2, 3]

