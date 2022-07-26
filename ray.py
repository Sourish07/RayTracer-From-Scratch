from point import Point
from vector import Vector


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

    def at(self, t):
        return self.origin + t * self.direction

    def __call__(self, t):
        return self.at(t)
