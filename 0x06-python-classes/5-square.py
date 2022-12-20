#!/usr/bin/python3
class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialises the data"""
        self.size = size

    def area(self):
        """Returns current square area"""
        return self.__size**2
