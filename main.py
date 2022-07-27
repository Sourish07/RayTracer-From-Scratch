from color import Color
from point import Point
from ray import Ray
from scene import Scene
from sphere import Sphere
from vector import Vector
from light import Light
from plane import Plane
from cube import Cube
from material import Material, Glass
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
    if depth == 0:
        return color

    obj_hit, t = find_nearest_object(r, scene.objects)
    if t is None:
        return color
    hit_pos = r(t)
    normal = obj_hit.normal_at(hit_pos)
    hit_pos += normal * 0.001

    for light in scene.lights:
        light_ray = Ray(hit_pos, light.pos - hit_pos)
        _, t = find_nearest_object(light_ray, scene.objects)
        if not t:
            # Direct path to light
            # Lambert cosine law
            color += obj_hit.material.color * \
                max(normal.dot(light_ray.direction), 0)

    bounce_ray = obj_hit.material.bounce(r, normal, hit_pos)
    assert(isinstance(bounce_ray, Ray))
    return color + color_ray(bounce_ray, scene, depth - 1) * 0.25


def render():
    HEIGHT = 360
    ASPECT_RATIO = 16 / 9
    WIDTH = int(HEIGHT * ASPECT_RATIO)

    MAX_DEPTH = 10
    NUM_SAMPLES = 20

    x0 = -1
    x1 = 1
    x_step = (x1 - x0) / (WIDTH - 1)
    y0 = x0 / ASPECT_RATIO
    y1 = x1 / ASPECT_RATIO
    y_step = (y1 - y0) / (HEIGHT - 1)

    camera = Point(x=0, y=0, z=1)
    red = Material(Color(1, 0, 0))
    green = Material(Color(0, 1, 0))
    blue = Material(Color(0, 0, 1))

    gold = Material(Color(0.8, 0.6, 0.2))
    silver = Material(Color(0.3, 0.3, 0.3))
    bronze = Material(Color(0.7, 0.3, 0.3), roughness=1)

    gray = Material(Color(0.5, 0.5, 0.5))
    objects = [Sphere(Point(0, 0, -1), 0.5, Glass()),
               Cube(Point(-1.25, 0, -1.5), 0.5, silver),
               Cube(Point(1.35, 0, -2), 0.5, bronze),
               Plane(Point(y=-0.5), Vector(y=1), gray)]

    # objects = [Sphere(Point(0, 0, -1), 0.5, gold),
    #            Sphere(Point(-1.25, 0, -1.5), 0.5, silver),
    #            Sphere(Point(1.35, 0, -2), 0.5, bronze),
    #            #Sphere(Point(0, -10000.5, 0), -10000, gray)]
    #            Plane(Point(y=-0.5), Vector(y=1), gray)]

    # objects = [Plane(Point(y=-0.5), Vector(y=1), gray),
    #            Cube(Point(1, 0, -2), 0.25, gold)]
    lights = [Light(Point(x=1, y=1, z=1)),
              Light(Point(x=-1, y=5, z=5))]

    scene = Scene(objects, lights, camera)

    with open("output-sk.ppm", "w") as f:
        f.write(f"P3\n{WIDTH} {HEIGHT}\n255\n")

        for j in range(HEIGHT - 1, -1, -1):
            print_progress_bar((HEIGHT - j) / HEIGHT)
            v = y0 + y_step * j
            for i in range(WIDTH):
                c = Color()
                u = x0 + x_step * i
                for _ in range(NUM_SAMPLES):
                    _u = u + (random() - 0.5) / (WIDTH - 1)
                    _v = v + (random() - 0.5) / (HEIGHT - 1)
                    r = Ray(camera, Point(_u, _v) - camera)
                    c += color_ray(r, scene, depth=MAX_DEPTH)
                c = c / NUM_SAMPLES
                write_color(f, c)


if __name__ == "__main__":
    render()
