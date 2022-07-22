from color import Color
from point import Point
from ray import Ray
from scene import Scene
from sphere import Sphere
from vector import Vector
from light import Light
from material import Material

def print_progress_bar(percentage):
    num = int(percentage * 20)
    print(f"[{'=' * num}{' ' * (20-num)}] {int(percentage * 100)}%", end='\r')
    
def clamp(n, _min, _max):
    return max(_min, min(n, _max))
    

def write_color(f, color):
    f.write(f"{int(255 * clamp(color.x, 0, 1))} {int(255 * clamp(color.y, 0, 1))} {int(255 * clamp(color.z, 0, 1))}\n")
    

def find_nearest_object(r, objects):
    distance = None
    obj = None
    for o in objects:
        t = o.hit(r)
        if t is None: continue
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
    
    #color += obj_hit.material.color
    #return color
    #print(color)
    for light in scene.lights:
        light_ray = Ray(hit_pos, light.pos - hit_pos)
        _, t = find_nearest_object(light_ray, scene.objects)
        if not t:
            # Direct path to light
            #print(light.color * max(normal.dot(light_ray.direction), 0))
            color += obj_hit.material.color * max(normal.dot(light_ray.direction), 0)
            
            #half_vector = (light_ray.direction + scene.camera).normalize()
            #color += light.color
            #print(color)
            #print("\n\n\n")
            
    bounce_ray = Ray(hit_pos, Vector.random())
    return color# + color_ray(bounce_ray, objects, lights, depth - 1) * 0.25
    #return color_at(obj_hit, r(t), normal, objects, lights)


#def color_at(obj, pos, normal, objects, lights):
    
    

def render():
    HEIGHT = 240
    ASPECT_RATIO = 16 / 9
    WIDTH = int(HEIGHT * ASPECT_RATIO)
    
    MAX_DEPTH = 5
    
    x0 = -1
    x1 = 1
    x_step = (x1 - x0) / (WIDTH - 1)
    y0 = x0 / ASPECT_RATIO
    y1 = x1 / ASPECT_RATIO
    y_step = (y1 - y0) / (HEIGHT - 1)
    
    camera = Point(z=1)
    red = Material(Color(1, 0, 0))
    blue = Material(Color(0, 1, 0))
    green = Material(Color(0, 0, 1))
    gray = Material(Color(0.5, 0.5, 0.5))
    objects = [Sphere(Point(0, 0, -1), 0.5, red), 
               Sphere(Point(-1.25, 0, -1.5), 0.5, blue), 
               Sphere(Point(1.35, 0, -2), 0.5, green),
               Sphere(Point(0, -100000.5, 0), -100000, gray)]
    lights = [Light(Point(x=1, y=1, z=1))]
    
    scene = Scene(objects, lights, camera)
    
    with open("output.ppm", "w") as f:
        f.write(f"P3\n{WIDTH} {HEIGHT}\n255\n")
        
        for j in range(HEIGHT - 1, -1, -1):
            print_progress_bar((HEIGHT - j) / HEIGHT)
            v = y0 + y_step * j
            for i in range(WIDTH):
                u = x0 + x_step * i
                r = Ray(camera, Point(u, v) - camera)
                c = color_ray(r, scene, depth=MAX_DEPTH)
                write_color(f, c)


if __name__ == "__main__":
    render()