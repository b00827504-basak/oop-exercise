"""Simple examples of operator overloading in Python."""

from math import sqrt


# Problem 1: Add and subtract complex numbers.
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __str__(self):
        return f"{self.real} + ({self.imaginary})i"


# Problem 2: Compare people by age.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __gt__(self, other):
        return self.age > other.age


# Problem 4: Multiply vectors to get the dot product.
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


# Problem 5: Compare circles by radius.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius


# Problem 6: Compare points by distance from (0, 0).
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return self.distance() < other.distance()

    def __gt__(self, other):
        return self.distance() > other.distance()

    def __eq__(self, other):
        return self.distance() == other.distance()

    def __ne__(self, other):
        return self.distance() != other.distance()

    def __ge__(self, other):
        return self.distance() >= other.distance()

    def __le__(self, other):
        return self.distance() <= other.distance()


# Problem 7: Multiply two matrices.
class Matrix:
    def __init__(self, values):
        self.values = values

    def __mul__(self, other):
        a = self.values
        b = other.values
        if not a or not b or len(a[0]) != len(b):
            raise ValueError("The matrix sizes do not match.")

        result = []
        for row in a:
            new_row = []
            for column in range(len(b[0])):
                total = 0
                for k in range(len(b)):
                    total += row[k] * b[k][column]
                new_row.append(total)
            result.append(new_row)
        return Matrix(result)


if __name__ == "__main__":
    print("Problem 1:")
    print(ComplexNumber(3, 2) + ComplexNumber(1, 4))
    print(ComplexNumber(3, 2) - ComplexNumber(1, 4))

    print("Problem 2:")
    print(Person("Anna", 25, "female") > Person("Tom", 20, "male"))

    print("Problem 4:")
    print(Vector(1, 2, 3) * Vector(4, 5, 6))

    print("Problem 5:")
    circle1 = Circle(5)
    circle2 = Circle(3)
    print(circle1 > circle2, circle1 == circle2, circle1 <= circle2)

    print("Problem 6:")
    point1 = Point(3, 4)
    point2 = Point(1, 1)
    print(point1 > point2, point1 == point2)

    print("Problem 7:")
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    print((matrix1 * matrix2).values)
