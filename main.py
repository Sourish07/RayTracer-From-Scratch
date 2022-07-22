from color import Color
from point import Point
from ray import Ray
from sphere import Sphere
from vector import Vector

def write_color(f, color):
    f.write(f"{int(255.999 * color.x)} {int(255.999 * color.y)} {int(255.999 * color.z)}\n")
    
def color_ray(r, objects):
    for obj in objects:
        if obj.hit(r):
            return Color(1, 0, 0)
    # r = r.direction
    # t = 0.5*r.y+1
    # return (1 - t)*Color(1, 1, 1) + t*Color(0.5, 0.7, 1)
    return Color(0, 0, 0)


def render():
    HEIGHT = 240
    ASPECT_RATIO = 16 / 9
    WIDTH = int(HEIGHT * ASPECT_RATIO)
    
    viewport_height = 2
    viewport_width = viewport_height * ASPECT_RATIO
    focal_length = 1
    
    camera = Point()
    horizontal = Vector(x=viewport_width)
    vertical = Vector(y=viewport_height)
    lower_left_corner = camera - horizontal / 2 - vertical / 2 - Vector(0, 0, focal_length)
    objects = [Sphere(Point(0, 0, -1), 0.5)]
    
    with open("output.ppm", "w") as f:
        f.write(f"P3\n{WIDTH} {HEIGHT}\n255\n")
        
        for j in range(HEIGHT - 1, -1, -1):
            print(f"Lines remaining: {j}", end='\r')
            for i in range(WIDTH):
                u = i / (WIDTH - 1)
                v = j / (HEIGHT - 1)
                r = Ray(camera, lower_left_corner + horizontal * u + vertical * v - camera)
                c = color_ray(r, objects)
                write_color(f, c)


if __name__ == "__main__":
    render()