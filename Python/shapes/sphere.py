from math import sqrt

from shapes.shape import Shape


class Sphere(Shape):
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
            if t > 1e-3:
                return t
            t = (-b + sqrt(discriminant)) / 2*a
            if t > 1e-3:
                return t
        return None
    
    def normal_at(self, pos):
        return (pos - self.center).normalize()
    
    