from camera import Camera
from point import Point
from color import Color

from ray import Ray
import math
from shapes import *
from materials import *

class Scene:
    def __init__(self, objects=[], camera=Camera(), default_scene=None):
        self.objects = objects
        self.camera = camera

        if default_scene is not None:
            self.objects = self.get_default_scene(default_scene)
        
    def get_default_scene(self, num):
        red = Diffuse(Color(1, 0, 0))
        pink = Diffuse(Color(255, 87, 51))
        lavender = Diffuse(Color(223, 150, 150))
        green = Diffuse(Color(0, 1, 0))
        blue = Diffuse(Color(0, 0, 1))

        gold = Metal(Color(0.8, 0.6, 0.2))
        silver = Metal(Color(0.8, 0.8, 0.8), roughness=0.3)
        bronze = Metal(Color(0.7, 0.3, 0.3))
        glass = Glass()

        gray = Diffuse(Color(0.8, 0.8, 0.8))
        ground = Diffuse(Color(0.5, 0.5, 0.5))
        
        ground = Diffuse(Color(0.8, 0.8, 0))
        material_center = Diffuse(Color(0.1, 0.2, 0.5))
        
        return {
            0: [
                Sphere(Point(-2.5, 0, -2), 0.5, silver),
                Sphere(Point(1.5, 0.5, -1.5), 0.25, red),
                Sphere(Point(0, -1002, -1), 1000, ground),
                Sphere(Point(0, 0.25, -2.5), 1, glass),
                Sphere(Point(-1, 3.5, -2), 1.5, Emissive(intensity=25))
            ],
            1: [
                Sphere(Point(-2.5, 0, -2), 0.5, silver),
                Sphere(Point(-0.5, 1, -1.5), 0.25, gold),
                Sphere(Point(1.5, 0.5, -1.5), 0.25, red),
                Sphere(Point(0, -1002, -1), 1000, ground),
                Sphere(Point(0, 0.1, -2.5), 1, glass),
                Sphere(Point(-1, 3.5, -2), 1.5, Emissive(intensity=25))
            ],
            2: [
                Sphere(Point(0, 0, -3), 1, bronze),
                Sphere(Point(0.75, 0, -5), 0.5, red),
                RectangleXZ(-1, 1, -2, -3, 3, Emissive(intensity=25)),
                Sphere(Point(0, 3, -2), 1, Emissive(intensity=25)),
                Cube(Point(2, 0, -3), 0.5, silver),
                Sphere(Point(-1.5, 0, -1.5), 0.5, gold),
                Plane(Point(y=-5), Vector(y=1), gray)
            ],
            3: [
                Sphere(Point(0, -100.5, -0), 100, Diffuse(Color(0.8, 0.8, 0))),
                Sphere(Point(z=-0), 0.5, Diffuse(Color(0.7, 0.3, 0.3))),
                Sphere(Point(x=-1, z=-0), 0.5, Metal(Color(0.8, 0.8, 0.8))),
                Sphere(Point(x=1, z=-0), 0.5, Metal(Color(0.8, 0.6, 0.2)))
            ],
            4: [
                Sphere(Point(0, -100.5, -0), 100, ground),
                Sphere(Point(z=-0), 0.5, material_center),
                Sphere(Point(x=-1, z=-0), 0.5, glass),
                Sphere(Point(x=1, z=-0), 0.5, gold)
            ],
            5: [
                Sphere(Point(0, -100.5, -1), 100, ground),
                Sphere(Point(-0.5, 0, -0.5), 0.5, glass),
                Sphere(Point(0.75, 0, -0.5), 0.3, gold),
                Sphere(Point(1, 1, -1), 0.5, gold)
            ],
            6: [
                Plane(Point(y=-0.5), Vector(y=1), lavender),
                Sphere(Point(1.5, 6, -5), 1, Emissive(intensity=25)),
                Sphere(Point(0.7, 0, -0.75), 0.5, Glass()),
                Cube(Point(-0.7, 0, -0.75), 0.5, gold)
            ],
            7: [
                Sphere(Point(0, -100.5, -2), 100, ground),
                Sphere(Point(-0.5, 0, -1.5), 0.5, glass),
                Sphere(Point(0.75, 0, -1.5), 0.3, gold),
                Sphere(Point(1, 3, -2), 0.5, gold),
            ],
            8: [
                Plane(Point(y=-0.5), Vector(y=1), Diffuse(Color(0.6, 0.5, 0.5))),
                Sphere(Point(1.5, 6, -5), 1, Emissive(intensity=25)),
                Sphere(Point(0.7, 0, -0.75), 0.25, Glass()),
                Sphere(Point(-0.7, 0, -0.75), 0.5, Glass()),
                Sphere(Point(0.2, 0, -2), 0.5, gold),
            ],
            9: [
                Sphere(Point(0, -100.5, -2), 100, Diffuse(Color(0.5, 0.5, 0.5))),
                Sphere(Point(-0.5, 0, -1.5), 0.5, Glass()),
                Sphere(Point(0.75, 0, -1.5), 0.3, Metal(Color(0.8, 0.6, 0.2))),
                Sphere(Point(1, 3, -2), 0.5, Emissive(intensity=25))
            ]
        }[num]
        

        