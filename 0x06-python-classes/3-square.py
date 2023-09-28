#!/usr/bin/python3


class Square():
    """Defines a square."""

    def __init__(self, size=0):
        
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
