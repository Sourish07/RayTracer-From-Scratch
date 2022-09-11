from point import Point
from utilities import degrees_to_radians
from math import tan
from vector import Vector
from ray import Ray

class Camera():
    def __init__(self, aspect_ratio=16/9, fov=60, focal_length=1, origin=Point(z=1)):
        self.aspect_ratio = aspect_ratio
        theta = degrees_to_radians(fov)
        h = tan(theta / 2)
        self.viewport_height = 2 * h
        self.viewport_width = aspect_ratio * self.viewport_height
        self.focal_length = focal_length
        
        self.origin = origin
        self.horizontal = Vector(x=self.viewport_width)
        self.vertical = Vector(y=self.viewport_height)
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - Vector(z=self.focal_length)
        
    def get_ray(self, u, v):
        return Ray(self.origin, self.lower_left_corner + u * self.horizontal + v * self.vertical - self.origin)