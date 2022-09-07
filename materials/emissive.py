from materials.material import *

class Emissive(Material):
    def __init__(self, color=Color(1, 1, 1), intensity=5):
        super().__init__(color)
        self.color *= intensity

    def bounce(self, r, normal, hit_pos):
        return None

    def emitted(self):
        return self.color