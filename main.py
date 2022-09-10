from renderer import render
from scene import Scene
from time import time

if __name__ == "__main__":
    #for i in range(10):
    #t = time()

    for i in [9]:
        print('Rendering default scene number', i)
        scene = Scene(default_scene=i)
        render(scene, output=f'outputs/output{i}', quality=3)
        #print(time() - t)
