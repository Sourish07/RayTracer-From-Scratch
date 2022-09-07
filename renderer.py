from color import Color

from scene import Scene



#from light import Light
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
    
    if t is None:
        return Color()
        # unit_direction = r.direction.normalize()
        # t = 0.5 * (unit_direction.y + 1)
        # return (1.0 - t)*Color(1, 1, 1) + t * Color(0.5, 0.7, 1)

    hit_pos = r(t)
    normal = obj_hit.normal_at(hit_pos)
    color = obj_hit.material.color

    bounce_ray = obj_hit.material.bounce(r, normal, hit_pos)
    emitted = obj_hit.material.emitted()
    if not bounce_ray:
        return emitted

    return emitted + color * color_ray(bounce_ray, scene, depth - 1)


def render():
    HEIGHT = 720
    ASPECT_RATIO = 16 / 9
    WIDTH = int(HEIGHT * ASPECT_RATIO)

    MAX_DEPTH = 50
    NUM_SAMPLES = 15000

    scene = Scene(default_scene=8)

    with open("outputs/output3.ppm", "w") as f:
        f.write(f"P3\n{WIDTH} {HEIGHT}\n255\n")

        for j in range(HEIGHT - 1, -1, -1):
            print_progress_bar((HEIGHT - j) / HEIGHT)
            #v = y0 + y_step * j
            for i in range(WIDTH):
                c = Color()
                #u = x0 + x_step * i
                for _ in range(NUM_SAMPLES):
                    u = (i + random()) / (WIDTH - 1)
                    v = (j + random()) / (HEIGHT - 1)
                    r = scene.camera.get_ray(u, v)
                    #r = Ray(camera, Point(_u, _v) - camera)
                    c += color_ray(r, scene, depth=MAX_DEPTH)
                c /= NUM_SAMPLES
                write_color(f, c)