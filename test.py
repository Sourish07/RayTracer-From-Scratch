import raytracer as rt

redMat = rt.materials.Diffuse([1, 0, 0])
redMat = rt.materials.Glass([1, 0.5, 0.5], 1.5)
lightMat = rt.materials.Emissive([1, 1, 1], 3)
sphere1 = rt.shapes.Sphere([0, 0, -1], 0.5, redMat)
sphere2 = rt.shapes.Sphere([1, 0, -2], 0.5, lightMat)

groundMat = rt.materials.Diffuse([0.5, 0.5, 0.5])
ground = rt.shapes.Sphere([0, -100.5, -1], 100, groundMat)

camera = rt.Camera([0, 0, 1], 16/9, 60, 1)

renderer = rt.Renderer(360, samples_per_pixel=100, max_depth=25, background=[0, 0, 0], aspect_ratio=16/9) #0.5, 0.7, 1

renderer.add_shape(sphere1)
renderer.add_shape(sphere2)
renderer.add_shape(ground)

# renderer.render(camera, output_filename="output.ppm")

renderer2 = rt.Renderer(360, samples_per_pixel=100, max_depth=25, background=[0.5, 0.7, 1], aspect_ratio=16/9)

sphere = rt.shapes.Sphere([0, 0, -1], 0.5, rt.materials.Metal([0.8, 0.6, 0.2], 0))
renderer2.add_shape(sphere)
renderer2.add_shape(ground)

renderer2.render(camera, output_filename="output2.ppm")
