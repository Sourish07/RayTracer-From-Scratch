import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def random_points_in_unit_sphere():
    while True:
        x = np.random.random() * 2 - 1
        y = np.random.random() * 2 - 1
        z = np.random.random() * 2 - 1
        if x**2 + y**2 + z**2 <= 1:
            return np.array([x, y, z])
        
def random_points_on_unit_sphere():
    while True:
        x = np.random.random() * 2 - 1
        y = np.random.random() * 2 - 1
        z = np.random.random() * 2 - 1
        if x**2 + y**2 + z**2 <= 1:
            return np.array([x, y, z]) / np.sqrt(x**2 + y**2 + z**2)
        
def random_points_from_unit_cube():
    x = np.random.random() * 2 - 1
    y = np.random.random() * 2 - 1
    z = np.random.random() * 2 - 1
    return np.array([x, y, z]) / np.sqrt(x**2 + y**2 + z**2)


def random_points_from_cosine_sphere():
    u = np.random.random()
    v = np.random.random()

    z = np.sqrt(1 - v)

    phi = 2 * np.pi * u
    x = np.cos(phi) * np.sqrt(v)
    y = np.sin(phi) * np.sqrt(v)

    return np.array([x, y, z])



def visualize_points_on_sphere(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1, 1, 1])

    x, y, z = zip(*points)
    ax.axes.set_xlim3d(left=-1., right=1)
    ax.axes.set_ylim3d(bottom=-1., top=1) 
    ax.axes.set_zlim3d(bottom=-1., top=1) 
    ax.scatter(x, y, z, s=1, c='b', marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

if __name__ == '__main__':
    num_points = 40000
    points = []
    for i in range(num_points):
        points.append(random_points_from_cosine_sphere())
    visualize_points_on_sphere(points)
