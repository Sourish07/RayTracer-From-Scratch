from materials.material import *

class Diffuse(Material):
    def bounce(self, r, normal, hit_pos):
        target = hit_pos + normal + Vector.random_unit_vector()
        return Ray(hit_pos, target - hit_pos)