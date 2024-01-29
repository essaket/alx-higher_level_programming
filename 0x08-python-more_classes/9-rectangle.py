#!/usr/bin/python3
"""
Write an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """Defines an empty Rectangle"""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Inisializes the Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width private attribute value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width private attribute value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height private attribute value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height private attribute value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Reruns the Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the current Rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """retrns a rectangle with the character '#'"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += "\n"
        return rec_str[:-1]

    def __repr__(self):
        """return a string representation of the rectangle to be able
        to recreate a new instance
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print a message for del"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance"""
        return cls(size, size)
