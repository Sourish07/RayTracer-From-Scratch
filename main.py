from ctypes import pointer
from color import Color
from point import Point
from ray import Ray
from scene import Scene
from sphere import Sphere
from vector import Vector
from light import Light
from plane import Plane
from rectangle import RectangleXY, RectangleXZ, RectangleYZ
from cube import Cube
from material import Diffuse, Metal, Glass, Emissive
from random import random
from utilities import print_progress_bar, write_color


def find_nearest_object(r, objects):
    distance = None
    obj = None
    for o in objects:
        t = o.hit(r)
        if t is None:
            continue
        if distance is None or t < distance:
            distance = t
            obj = o
    return obj, distance


def color_ray(r, scene, depth):
    color = Color(0, 0, 0)
    if depth <= 0:
        return color

    obj_hit, t = find_nearest_object(r, scene.objects)
    if t is None:
        unit_direction = r.direction.normalize()
        t = 0.5 * (unit_direction.y + 1)
        return (1.0 - t)*Color(1, 1, 1) + t * Color(0.5, 0.7, 1)

    hit_pos = r(t)
    normal = obj_hit.normal_at(hit_pos)
    color = obj_hit.material.color

    bounce_ray = obj_hit.material.bounce(r, normal, hit_pos)
    emitted = obj_hit.material.emitted()
    if not bounce_ray:
        return emitted

    return emitted + color * color_ray(bounce_ray, scene, depth - 1)


def render():
    HEIGHT = 225
    ASPECT_RATIO = 16 / 9
    WIDTH = int(HEIGHT * ASPECT_RATIO)

    MAX_DEPTH = 50
    NUM_SAMPLES = 100

    x0 = -1.7777778
    x1 = 1.7777778
    x_step = (x1 - x0) / (WIDTH - 1)
    y0 = x0 / ASPECT_RATIO
    y1 = x1 / ASPECT_RATIO
    y_step = (y1 - y0) / (HEIGHT - 1)

    camera = Point(x=0, y=0, z=1)
    red = Diffuse(Color(1, 0, 0))
    pink = Diffuse(Color(255, 87, 51))
    green = Diffuse(Color(0, 1, 0))
    blue = Diffuse(Color(0, 0, 1))

    gold = Metal(Color(0.8, 0.6, 0.2))
    silver = Metal(Color(0.8, 0.8, 0.8), roughness=0.3)
    bronze = Metal(Color(0.7, 0.3, 0.3))
    glass = Glass()

    gray = Diffuse(Color(0.8, 0.8, 0.8))
    ground = Diffuse(Color(0.5, 0.5, 0.5))

    num = 3
    if num == 0:
        objects = [
            Sphere(Point(-2.5, 0, -2), 0.5, silver),
            Sphere(Point(1.5, 0.5, -1.5), 0.25, red),
            Sphere(Point(0, -1002, -1), 1000, ground),
            Sphere(Point(0, 0.25, -2.5), 1, glass),
            Sphere(Point(-1, 3.5, -2), 1.5, Emissive())
        ]
    elif num == 1:
        objects = [
            Sphere(Point(-2.5, 0, -2), 0.5, silver),
            #Sphere(Point(-0.5, 1, -1.5), 0.25, gold),
            Sphere(Point(1.5, 0.5, -1.5), 0.25, red),
            Sphere(Point(0, -1002, -1), 1000, ground),
            Sphere(Point(0, 0.25, -2.5), 1, gold),
            #Sphere(Point(0, 0.25, -3.5), 0.25, gold),
            Sphere(Point(-1, 3.5, -2), 1.5, Emissive())
        ]
    elif num == 2:
        objects = [
            Sphere(Point(0, 0, -3), 1, bronze),
            Sphere(Point(0.75, 0, -5), 0.5, red),
            RectangleXZ(-1, 1, -2, -3, 3, Emissive(intensity=5)),
            Sphere(Point(0, 3, -2), 1, Emissive(intensity=100)),
            Cube(Point(2, 0, -3), 0.5, silver),
            Sphere(Point(-1.5, 0, -1.5), 0.5, gold),
            Plane(Point(y=-5), Vector(y=1), gray)
        ]
    elif num == 3:
        material_ground = Diffuse(Color(0.8, 0.8, 0))
        material_center = Diffuse(Color(0.7, 0.3, 0.3))
        material_left = Metal(Color(0.8, 0.8, 0.8))
        #material_left = Glass(1.5)
        material_right = Metal(Color(0.8, 0.6, 0.2))
        objects = [
            Sphere(Point(0, -100.5, -0), 100, material_ground),
            Sphere(Point(z=-0), 0.5, material_center),
            Sphere(Point(x=-1, z=-0), 0.5, material_left),
            Sphere(Point(x=1, z=-0), 0.5, material_right)
        ]
    # objects = [Sphere(Point(0, 0, -1), 0.5, gold),
    #            Sphere(Point(-1.25, 0, -1.5), 0.5, silver),
    #            Sphere(Point(1.35, 0, -2), 0.5, bronze),
    #            #Sphere(Point(0, -10000.5, 0), -10000, gray)]
    #            Plane(Point(y=-0.5), Vector(y=1), gray)]

    # objects = [Plane(Point(y=-0.5), Vector(y=1), gray),
    #            Cube(Point(1, 0, -2), 0.25, gold)]
    
    # lights = [Light(Point(x=1, y=1, z=1)),
    #           Light(Point(x=-1, y=5, z=5))]
    #objects.append(Sphere(Point(-2.5, 2, -1), 2, Emissive()))

    scene = Scene(objects, [], camera)

    with open("output-sk5.ppm", "w") as f:
        f.write(f"P3\n{WIDTH} {HEIGHT}\n255\n")

        for j in range(HEIGHT - 1, -1, -1):
            print_progress_bar((HEIGHT - j) / HEIGHT)
            v = y0 + y_step * j
            for i in range(WIDTH):
                c = Color()
                u = x0 + x_step * i
                for _ in range(NUM_SAMPLES):
                    _u = u + (random() * 2 - 1) / (WIDTH - 1)
                    _v = v + ((random() * 2 - 1) / (HEIGHT - 1))
                    r = Ray(camera, Point(_u, _v) - camera)
                    c += color_ray(r, scene, depth=MAX_DEPTH)
                c /= NUM_SAMPLES
                write_color(f, c)


if __name__ == "__main__":
    render()
