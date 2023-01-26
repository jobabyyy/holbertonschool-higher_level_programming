#!/usr/bin/python3
def lookup(obj):
    return dir(obj)

class MyClass:
    def __init__(self):
        self.x = 5
        self.y = 10

    def my_method(self):
        return self.x + self.y

my_obj = MyClass()
print(lookup(my_obj))

