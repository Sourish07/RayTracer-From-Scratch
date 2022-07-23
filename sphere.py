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
            t = (-b - sqrt(discriminant)) / 2*a
            if t > 0:
                return t
        return None
    
    def normal_at(self, pos):
        return (pos - self.center).normalize()
    
    