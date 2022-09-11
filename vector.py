import math
from random import random
from utilities import random_double_in_range

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)            
        return Vector(self.x + other, self.y + other, self.z + other)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):
        return self + (other * -1)

    def __isub__(self, other):
        self += (other * -1)
        return self
    
    def __neg__(self):
        return -1 * self

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x * other, self.y * other, self.z * other)
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __rmul__(self, other):
        return self * other
    
    def __neg__(self):
        return Vector(self.x * -1 if not self.x == 0 else 0,
                      self.y * -1 if not self.y == 0 else 0,
                      self.z * -1 if not self.z == 0 else 0,)

    def __imul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.x *= other
            self.y *= other
            self.z *= other
        else:
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        return self

    def __itruediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.x /= other
            self.y /= other
            self.z /= other
        else:
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        return self
    
    def __truediv__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x / other.x, self.y / other.y, self.z / other.z)
        assert(isinstance(other, float) or isinstance(other, int))
        return Vector(self.x / other, self.y / other, self.z / other)

    def __itruediv__(self, other):
        if isinstance(other, Vector):
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        else:
            self.x /= other
            self.y /= other
            self.z /= other
        return self

    def length(self):
        return math.sqrt(self.length_squared())
    
    def length_squared(self):
        return self.x**2 + self.y**2 + self.z**2

    def normalize(self):
        return self / self.length()

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def near_zero(self):
        s = 1e-6
        return abs(self.x) < s and abs(self.y) < s and abs(self.z) < s

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"

    
    @classmethod
    def random(cls):
        x = random()
        y = random()
        z = random()
        return cls(x, y, z)
                    
    @classmethod
    def random(cls, min, max):
        x = random_double_in_range(min, max)
        y = random_double_in_range(min, max)
        z = random_double_in_range(min, max)
        return cls(x, y, z)
    
    @classmethod
    def random_in_unit_sphere(cls):
        while True:
            p = cls.random(-1, 1)
            if p.length_squared() >= 1:
                continue
            return p
        
    @classmethod
    def random_unit_vector(cls):
        return cls.random_in_unit_sphere().normalize()
