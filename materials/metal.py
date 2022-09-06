from materials.material import *

class Metal(Material):
    def __init__(self, color, roughness=0):
        super().__init__(color)
        self.roughness = roughness

    def bounce(self, r, normal, hit_pos):
        if random() > self.roughness:
            new_direction = r.direction - 2 * r.direction.dot(normal)*normal
            return Ray(hit_pos, new_direction)
        return Ray(hit_pos, Vector.random_unit_vector())