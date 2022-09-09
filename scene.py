from camera import Camera
from point import Point
from color import Color

from shapes import *
from materials import *

class Scene:
    def __init__(self, objects=None, camera=None, background=None, default_scene=None):
        self.objects = objects if objects is not None else []
        self.camera = camera if camera is not None else Camera()
        self.background = background if background is not None else lambda t: Color()

        if default_scene is not None:
            self.get_default_scene(default_scene)
        
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
        
        green_ground = Diffuse(Color(0.8, 0.8, 0))
        tan = Diffuse(Color(0.7, 0.3, 0.3))
        
        def default_background(dir):
            return Color()
        
        def gradient_background(dir):
            t = 0.5 * (dir.y + 1)
            return (1 - t) * Color(1, 1, 1) + t * Color(0.5, 0.7, 1)
        
        light = Emissive(intensity=25)
        
        self.objects, self.background = [ 
            ([
                Plane(Point(y=-0.5), Vector(y=1), gray),
                Sphere(Point(0, 0, -1), 0.5, red),
                Sphere(Point(-1.5, 2, -1), 0.5, Emissive(intensity=10))
            ], default_background), 
            ([
                Sphere(Point(-2.5, 0, -2), 0.5, silver),
                Sphere(Point(-0.5, 1, -1.5), 0.25, gold),
                Sphere(Point(1.5, 0.5, -1.5), 0.25, red),
                Sphere(Point(0, -1002, -1), 1000, ground),
                Sphere(Point(0, 0.1, -2.5), 1, glass),
                Sphere(Point(-1, 3.5, -2), 1.5, light)
            ], default_background), 
            ([
                Sphere(Point(0, 0, -3), 1, bronze),
                Sphere(Point(0, 3, -2), 1, light),
                Sphere(Point(2, 0, -3), 0.5, silver),
                Sphere(Point(-1.5, 0, -1.5), 0.5, gold),
                Plane(Point(y=-2), Vector(y=1), gray)
            ], default_background), 
            ([
                Sphere(Point(0, -100.5, -1), 100, green_ground),
                Sphere(Point(z=-1), 0.5, tan),
                Sphere(Point(x=-1, z=-1), 0.5, silver),
                Sphere(Point(x=1, z=-1), 0.5, gold)
            ], gradient_background), 
            ([
                Plane(Point(y=-0.5), Vector(y=1), Diffuse(Color(0.97, 0.94, 0.89))),
                Sphere(Point(1.5, 6, -5), 1, light),
                Sphere(Point(0.7, 0, -0.75), 0.5, glass),
                Cube(Point(-0.7, 0, -0.75), 0.5, glass)
            ], default_background), 
            ([
                Plane(Point(y=-0.5), Vector(y=1), Diffuse(Color(0.6, 0.5, 0.5))),
                Sphere(Point(1.5, 6, -5), 1, light),
                Sphere(Point(0.7, 0, -0.75), 0.25, glass),
                Sphere(Point(-0.7, 0, -0.75), 0.5, glass),
                Sphere(Point(0.2, 0, -2), 0.5, gold),
            ], default_background), 
            ([
                Sphere(Point(0, -100.5, -2), 100, ground),
                Sphere(Point(-0.5, 0, -1.5), 0.5, glass),
                Sphere(Point(0.75, 0, -1.5), 0.3, gold),
                Sphere(Point(1, 3, -2), 0.5, light)
            ], default_background), 
            ([
                Sphere(Point(0, -100.5, -2), 100, ground),
                Cube(Point(-0.5, 0, -1.5), 0.5, glass),
                ####Cube(Point(-0, 0, -1), 0.5, glass),
                Sphere(Point(0.75, 0, -1.5), 0.3, gold),
                Sphere(Point(1, 3, -2), 0.5, light)
            ], default_background)
        ][num]      
