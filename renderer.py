from color import Color
from scene import Scene
from shapes import *

from random import random
from utilities import print_progress_bar, write_color


def find_nearest_object(r, objects):
    """Iterates through all objects in a scene and calculates the closest object the ray has hit

    Args:
        r (Ray): The current ray being cast
        objects (List[Shapes]): A list of all current objects in scene

    Returns:
        tuple(Object, float): Return tuples pair for object that is the closest, along with t-value for ray. If t-value is None, no objects were hit
    """
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
    if depth == 0:
        return Color(0, 0, 0)

    obj_hit, t = find_nearest_object(r, scene.objects)
    # if isinstance(obj_hit, Cube):
    #     x = 10
    if t is None:
        return scene.background(r.direction)

    hit_pos = r(t)
    normal = obj_hit.normal_at(hit_pos)
    color = obj_hit.material.color

    bounce_ray = obj_hit.material.bounce(r, normal, hit_pos)
    emitted = obj_hit.material.emitted()
    if not bounce_ray:
        return emitted

    return emitted + color * color_ray(bounce_ray, scene, depth - 1)


def render(scene, output='outputs/output', quality=3):
    
    HEIGHT = [100, 240, 360, 720, 2160][quality]
    MAX_DEPTH = [5, 25, 50, 50, 100][quality]
    NUM_SAMPLES = [50, 50, 100, 10000, 15000][quality]
        
    ASPECT_RATIO = 16 / 9
    WIDTH = int(HEIGHT * ASPECT_RATIO)

    with open(f"{output}.ppm", "w") as f:
        f.write(f"P3\n{WIDTH} {HEIGHT}\n255\n")

        for j in range(HEIGHT - 1, -1, -1):
            print_progress_bar((HEIGHT - j) / HEIGHT)
            for i in range(WIDTH):
                c = Color()
                for _ in range(NUM_SAMPLES):
                    u = (i + random()) / (WIDTH - 1)
                    v = (j + random()) / (HEIGHT - 1)
                    r = scene.camera.get_ray(u, v)
                    c += color_ray(r, scene, depth=MAX_DEPTH)
                c /= NUM_SAMPLES
                write_color(f, c)