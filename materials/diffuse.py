from materials.material import *

class Diffuse(Material):
    def bounce(self, r, normal, hit_pos):
        new_direction = normal + Vector.random_unit_vector()
        if new_direction.near_zero():
            new_direction = normal
        return Ray(hit_pos, new_direction)