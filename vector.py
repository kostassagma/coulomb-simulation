from math import sqrt

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return (f"({self.x},{self.y})")

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(self.x*other, self.y*other)
        return self.x*other.x+self.y*other.y
    
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    
    def __abs__(self):
        return sqrt((self.x)**2+(self.y)**2)
