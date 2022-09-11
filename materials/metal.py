from materials.material import *

class Metal(Material):
    def __init__(self, color, fuzz=0):
        super().__init__(color)
        self.fuzz = fuzz

    def bounce(self, r, normal, hit_pos):
        new_direction = r.direction - 2 * r.direction.dot(normal)*normal + self.fuzz * Vector.random_in_unit_sphere()
        return Ray(hit_pos, new_direction)