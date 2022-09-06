from point import Point
from vector import Vector
from ray import Ray

class Camera():
    def __init__(self, aspect_ratio=16/9, vp_height=2, focal_length=1):
        self.aspect_ratio = aspect_ratio
        self.viewport_height = vp_height
        self.viewport_width = aspect_ratio * self.viewport_height
        self.focal_length = 1
        
        self.origin = Point()
        self.horizontal = Vector(x=self.viewport_width)
        self.vertical = Vector(y=self.viewport_height)
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - Vector(z=self.focal_length)
        
    def get_ray(self, u, v):
        return Ray(self.origin, self.lower_left_corner + u * self.horizontal + v * self.vertical - self.origin)