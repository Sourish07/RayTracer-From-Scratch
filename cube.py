from math import sqrt
from geometry import Geometry
from vector import Vector

class Cube(Geometry):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material
        self.min = self.center - Vector(radius, radius, radius)
        self.max = self.center + Vector(radius, radius, radius)
    
    def hit(self, r):
        t0 = (self.min - r.origin) / (r.direction)
        t1 = (self.max - r.origin) / (r.direction)
        
        t_min = max(min(t0.x, t1.x), min(t0.y, t1.y), min(t0.z, t1.z))
        t_max = min(max(t0.x, t1.x), max(t0.y, t1.y), max(t0.z, t1.z))
        
        if t_min <= t_max:
            if t_min > 1e-6:
                return t_min
            elif t_max > 1e-6:
                return t_max
        return None
    
    def normal_at(self, pos):
        pos -= self.center
        pos = pos.normalize()
        nums = [(pos.dot(Vector(x=1)), Vector(x=1)),
                (pos.dot(Vector(y=1)), Vector(y=1)),
                (pos.dot(Vector(z=1)), Vector(z=1)),
                (pos.dot(Vector(x=-1)), Vector(x=-1)),
                (pos.dot(Vector(y=-1)), Vector(y=-1)),
                (pos.dot(Vector(z=-1)), Vector(z=-1))]
        
        return max(nums, key=lambda x: x[0])[1]
         
    
    