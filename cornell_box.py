import raytracer as rt

redMat = rt.materials.Diffuse([1, 0, 0])
blueMat = rt.materials.Diffuse([0, 0, 1])
goldMat = rt.materials.Metal([0.8, 0.6, 0.2], fuzz=0)
whiteMat = rt.materials.Diffuse([0.7, 0.7, 0.7])
lightMat = rt.materials.Emissive([1, 1, 1], 15)
glassMat = rt.materials.Glass([1, 1, 1], 1.5)

left_wall = rt.shapes.RectangleYZ(-1, 1, -1, 1, -1, redMat)
right_wall = rt.shapes.RectangleYZ(-1, 1, -1, 1, 1, blueMat, flipNormal=True)
top_wall = rt.shapes.RectangleXZ(-1, 1, -1, 1, 1, whiteMat, flipNormal=True)
bottom_wall = rt.shapes.RectangleXZ(-1, 1, -1, 1, -1, whiteMat)
back_wall = rt.shapes.RectangleXY(-1, 1, -1, 1, -1, whiteMat)

light = rt.shapes.RectangleXZ(-0.2, 0.2, -0.2, 0.2, 0.99, lightMat)

small_box = rt.shapes.Cube([-0.4, -0.6, -0.1], 0.3, whiteMat)
gold_sphere = rt.shapes.Sphere([0, 0.3, -0.5], 0.3, goldMat)
glass_sphere = rt.shapes.Sphere([0.3, -0.5, 0.4], 0.3, glassMat)

camera = rt.Camera([0, 0, 3], 16 / 9, 60, 1)

renderer = rt.Renderer(1080, samples_per_pixel=10000, max_depth=50, background=[0, 0, 0], aspect_ratio=16 / 9)

renderer.add_shape(left_wall)
renderer.add_shape(right_wall)
renderer.add_shape(top_wall)
renderer.add_shape(bottom_wall)
renderer.add_shape(back_wall)
renderer.add_shape(light)
renderer.add_shape(small_box)
renderer.add_shape(gold_sphere)
renderer.add_shape(glass_sphere)

renderer.render(camera, output_filename="cornell_box.ppm")
