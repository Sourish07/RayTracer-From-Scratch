from math import sqrt


class Plane:
    def __init__(self, point, normal, material):
        self.point = point
        self.normal = normal
        self.material = material
        
    def hit(self, r):
        t = ((self.point - r.origin).dot(self.normal)) / (r.direction.dot(self.normal))
        if t > 0:
            return t
        return None
    
    def normal_at(self, pos):
        return self.normal
    
    