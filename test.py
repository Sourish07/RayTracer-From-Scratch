import raytracer as rt

redMat = rt.materials.Diffuse([1, 0, 0])
blueMat = rt.materials.Diffuse([0, 0, 1])
whiteMat = rt.materials.Diffuse([0.7, 0.7, 0.7])
glassMat = rt.materials.Glass([1, 0.5, 0.5], 1.5)
goldMat = rt.materials.Metal([0.8, 0.6, 0.2], 0)
lightMat = rt.materials.Emissive([1, 1, 1], 30)

left_wall = rt.shapes.RectangleYZ(-1, 1, -1, 1, -1, redMat)
right_wall = rt.shapes.RectangleYZ(-1, 1, -1, 1, 1, blueMat, flipNormal=True)
sphere = rt.shapes.Sphere([0, 0, 0], 0.25, glassMat)
light = rt.shapes.RectangleXZ(-0.2, 0.2, -0.2, 0.2, 0.99, lightMat)
# ground = rt.shapes.Plane([0, -0.5, 0], [0, 1, 0], whiteMat)
ground = rt.shapes.Sphere([0, -1000.5, 0], 1000, whiteMat)
ground = rt.shapes.RectangleXZ(-1, 1, -1, 1, -1, whiteMat)

camera = rt.Camera([0, 0, 3], 1, 60, 1)

renderer = rt.Renderer(360, samples_per_pixel=100, max_depth=25, background=[0.0, 0.0, 0.0], aspect_ratio=1)

renderer.add_shape(left_wall)
renderer.add_shape(right_wall)
renderer.add_shape(sphere)
renderer.add_shape(light)
renderer.add_shape(ground)

renderer.render(camera, output_filename="test.ppm")
