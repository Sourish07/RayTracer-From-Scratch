from vector import Vector
from ray import Ray
from random import random


class Material:
    def __init__(self, color, roughness=0):
        self.color = color
        self.roughness = roughness

    def bounce(self, r, normal, hit_pos):
        if random() > self.roughness:
            new_direction = r.direction - 2 * r.direction.dot(normal)*normal
            return Ray(hit_pos, new_direction)
        return Ray(hit_pos, Vector.random())
