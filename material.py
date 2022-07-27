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
        refraction_ratio = self.idx_refraction if not outside else 1 / self.idx_refraction
        
        refracted_ray = self.refract(r.direction, normal if outside else -1 * normal, refraction_ratio)
        return Ray(hit_pos, refracted_ray)
    
    def refract(self, direction, normal, refraction_ratio):
        cos_theta = min((-1 * direction).dot(normal), 1)
        perp = refraction_ratio * (direction + cos_theta * normal)
        parallel = -sqrt(abs(1 - perp.length()**2)) * normal
        
        return parallel + perp
    
    # def reflectance(self, cos, reflectance_ratio):
    #     r0 = (1 - reflectance_ratio) / (1 + reflectance_ratio)
    #     r0 = r0 **2
    #     return r0 + (1 - r0) * pow((1 - cos), 5)