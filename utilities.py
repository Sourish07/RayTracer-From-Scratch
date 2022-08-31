from math import sqrt

def print_progress_bar(percentage):
    num = int(percentage * 20)
    print(f"[{'=' * num}{' ' * (20-num)}] {int(percentage * 100)}%", end='\r')


def clamp(n, _min, _max):
    return max(_min, min(n, _max))


def write_color(f, color):
    f.write(f"{int(255 * clamp(sqrt(color.x), 0, 1))} {int(255 * clamp(sqrt(color.y), 0, 1))} {int(255 * clamp(sqrt(color.z), 0, 1))}\n")
