#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py).

    Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
    the area() method must be implemented

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle, who inherits from BaseGeometry
    methods:
        __init__(self, size)
        __str__(self)
    """

    def __init__(self, size):
        """initializes size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints rectangle description
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
