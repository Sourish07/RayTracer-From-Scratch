from math import sqrt, pi
from random import random

def print_progress_bar(percentage):
    num = int(percentage * 20)
    print(f"[{'=' * num}{' ' * (20-num)}] {int(percentage * 100)}%", end='\r')


def clamp(n, _min, _max):
    return max(_min, min(n, _max))


def write_color(f, color):
    f.write(f"{int(256 * clamp(sqrt(color.x), 0, 0.999))} {int(256 * clamp(sqrt(color.y), 0, 0.999))} {int(256 * clamp(sqrt(color.z), 0, 0.999))}\n")

def random_double_in_range(min, max):
    return min + (max - min) * random()


def degrees_to_radians(degrees):
    return degrees * pi / 180