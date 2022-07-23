import math
from random import random


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x + other, self.y + other, self.z + other)
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):
        # return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return self + (-1 * other)

    def __isub__(self, other):
        self += (other * -1)
        return self

    def __mul__(self, other):
        assert(isinstance(other, float) or isinstance(other, int))
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        assert(isinstance(other, float))
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z
        return self

    def __itruediv__(self, other):
        assert(isinstance(other, float))
        self.x /= other.x
        self.y /= other.y
        self.z /= other.z
        return self

    def __truediv__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x / other.x, self.y / other.y, self.z / other.z)
        assert(isinstance(other, float) or isinstance(other, int))
        return Vector(self.x / other, self.y / other, self.z / other)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        return self / self.length()

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"

    @classmethod
    def random(cls):
        while True:
            x = (random() - 0.5) * 2
            y = (random() - 0.5) * 2
            z = (random() - 0.5) * 2
            v = cls(x, y, z)
            if v.length() <= 1:
                return v.normalize()
