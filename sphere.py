from sympy import discriminant


class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        
    def hit(self, r):
        oc = r.origin - self.center
        a = r.direction.dot(r.direction)
        b = 2 * oc.dot(r.direction)
        c = oc.dot(oc) - self.radius**2
        discriminant = b**2 - 4 * a * c
        # print(discriminant)
        return discriminant > 0