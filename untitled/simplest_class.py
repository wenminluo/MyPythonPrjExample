# Filename e:simplest_class.py

""" Simple class test """
__version__ = '1.0'


class Person:
    """ Class person """

    def __init__(self, name):
        self.name = name;

    # pass # An empty block
    def SayHi(self):
        print("Hello,my name is", self.name);
