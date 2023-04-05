import raytracer as rt

redMat = rt.materials.Diffuse([1, 0, 0])
glassMat = rt.materials.Glass([1, 0.5, 0.5], 1.5)
goldMat = rt.materials.Metal([0.8, 0.6, 0.2], 0)
lightMat = rt.materials.Emissive([1, 1, 1], 3)


sphere1 = rt.shapes.Cube([0, 0, -1], 0.5, glassMat)
topLight = rt.shapes.RectangleXZ(-0.25, 0.25, -1.75, -1.25, 0.99, lightMat)
groundMat = rt.materials.Diffuse([0.5, 0.5, 0.5])
ground = rt.shapes.Sphere([0, -100.5, -1], 100, groundMat)

camera = rt.Camera([0, 0, 1], 16/9, 60, 1)

renderer = rt.Renderer(240, samples_per_pixel=50, max_depth=10, background=[0.1, 0.1, 0.1], aspect_ratio=16/9) #0.5, 0.7, 1

renderer.add_shape(sphere1)
renderer.add_shape(topLight)
renderer.add_shape(ground)

renderer.render(camera, output_filename="output.ppm")

renderer2 = rt.Renderer(240, samples_per_pixel=10, max_depth=25, background=[0.5, 0.7, 1], aspect_ratio=16/9)

sphere = rt.shapes.Cube([3, 0, -3], 0.5, glassMat)
renderer2.add_shape(sphere)
renderer2.add_shape(ground)

# renderer2.render(camera, output_filename="output2.ppm")
