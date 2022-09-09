from renderer import render
from scene import Scene

if __name__ == "__main__":
    #for i in range(10):
    for i in [2]:
        print('Rendering default scene number', i)
        scene = Scene(default_scene=i)
        render(scene, output=f'outputs/output{i}', quality=1)
