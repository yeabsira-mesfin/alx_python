class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def perimeter(self):
        return 4 * self.__size

    def __str__(self):
        return f"Square with side length {self.__size}"

# Test the Square class
try:
    square1 = Square(5)
    print(square1)
    print("Area:", square1.area())
    print("Perimeter:", square1.perimeter())

    square2 = Square(-2)  # This will raise a ValueError
except ValueError as ve:
    print(ve)

try:
    square3 = Square("hello")  # This will raise a TypeError
except TypeError as te:
    print(te)