from shapes.shape import *


class RectangleXY(Shape):
    def __init__(self, x0, x1, y0, y1, z, material):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z = z
        self.material = material

    def hit(self, r):
        t = (self.z - r.origin.z) / r.direction.z
        hit_pos = r.origin + (r.direction * t)
        if hit_pos.x < self.x1 and hit_pos.x > self.x0 and hit_pos.y > self.y0 and hit_pos.y < self.y1:
            return t
        return None

    def normal_at(self, pos):
        # return (pos - self.center).normalize()
        return Vector(z=1)


class RectangleXZ(Shape):
    def __init__(self, x0, x1, z0, z1, y, material):
        self.x0 = x0
        self.x1 = x1
        self.z0 = min(z0, z1)
        self.z1 = max(z0, z1)
        self.y = y
        self.material = material

    def hit(self, r):
        t = (self.y - r.origin.y) / r.direction.y
        hit_pos = r.origin + (r.direction * t)
        if hit_pos.x < self.x1 and hit_pos.x > self.x0 and hit_pos.z > self.z0 and hit_pos.z < self.z1:
            return t
        return None

    def normal_at(self, pos):
        # return (pos - self.center).normalize()
        return Vector(y=-1)


class RectangleYZ(Shape):
    def __init__(self, y0, y1, z0, z1, x, material):
        self.y0 = y0
        self.y1 = y1
        self.z0 = min(z0, z1)
        self.z1 = max(z0, z1)
        self.x = x
        self.material = material

    def hit(self, r):
        t = (self.x - r.origin.x) / r.direction.x
        hit_pos = r.origin + (r.direction * t)
        if hit_pos.z < self.z1 and hit_pos.z > self.z0 and hit_pos.y > self.y0 and hit_pos.y < self.y1:
            return t
        return None

    def normal_at(self, pos):
        # return (pos - self.center).normalize()
        return Vector(x=-1)
