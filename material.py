from vector import Vector
from ray import Ray
from random import random
from math import sqrt
from color import Color

class Material:
    def __init__(self, color, roughness=0):
        self.color = color
        self.roughness = roughness

    def bounce(self, r, normal, hit_pos):
        if random() > self.roughness:
            new_direction = r.direction - 2 * r.direction.dot(normal)*normal
            return Ray(hit_pos, new_direction)
        return Ray(hit_pos, Vector.random())

class Glass(Material):
    def __init__(self, color=Color(1, 1, 1), idx_refraction=1.5):
        super().__init__(color)
        self.idx_refraction = idx_refraction
    
    def bounce(self, r, normal, hit_pos):
        outside = r.direction.dot(normal) < 0
        refraction_ratio = self.idx_refraction if outside else 1 / self.idx_refraction
        
        # cos_theta = min(-(r.direction).dot(normal), 1)
        # sin_theta = sqrt(1 - cos_theta**2)
        
        # cannot_refract = refraction_ratio * sin_theta > 1
        
        # if cannot_refract:
        #     return super().bounce(r, normal, hit_pos)
        
        refracted_ray = self.refract(r.direction, normal, refraction_ratio)
        return Ray(r.origin, refracted_ray)
    
    def refract(self, direction, normal, refraction_ratio):
        cos_theta = min(-direction.dot(normal), 1)
        r_out_perp = refraction_ratio * (direction + cos_theta*normal)
        r_out_parallel = -sqrt(abs(1 - r_out_perp.length() ** 2)) * normal
        return r_out_perp + r_out_parallel