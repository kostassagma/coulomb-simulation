from math import sqrt

class Vector:
    def __init__(self, x, y, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def cross_product(self, other):
        x = self.y*other.z-self.z*other.y
        y = self.z*other.x-self.x*other.z
        z = self.x*other.y-self.y*other.x
        return Vector(x, y, z=z)

    def __str__(self) -> str:
        return (f"({self.x},{self.y})")

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(self.x*other, self.y*other, z=self.z*other)
        return self.x*other.x+self.y*other.y

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, z=self.z+other.z)

    def __abs__(self):
        return sqrt((self.x)**2+(self.y)**2+(self.z)**2)
