class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.__height = height
        self.integer_validator("width", self.width)
        self.integer_validator("height", self.__height)

    def area(self):
        return self.width * self.__height

    def integer_validator(self, name, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")

    def __str__(self):
        return f"[Rectangle] {self.width}/{self.__height}"

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        return self.__size ** 2