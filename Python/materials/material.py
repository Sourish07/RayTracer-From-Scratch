from abc import ABC, abstractmethod
from vector import Vector
from ray import Ray
from random import random
from math import sqrt
from color import Color


class Material(ABC):
    def __init__(self, color):
        self.color = color
        if self.color.x > 1:
            self.color /= 255

    def color(self):
        return self.color

    @abstractmethod
    def bounce(self, r, normal, hit_pos):
        raise NotImplementedError

    def emitted(self):
        return Color(0, 0, 0)












