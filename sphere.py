from math import sqrt


class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material
        
    def hit(self, r):
        oc = r.origin - self.center
        a = r.direction.dot(r.direction)
        b = 2 * oc.dot(r.direction)
        c = oc.dot(oc) - self.radius**2
        discriminant = b**2 - 4 * a * c
        
        if discriminant > 0:
            min_root = (-b - sqrt(discriminant)) / 2*a
            if min_root > 0:
                return min_root
        return None
    
    def normal_at(self, pos):
        return (pos - self.center).normalize()