import raytracer as rt

redMat = rt.materials.Diffuse([1, 0, 0])
redMat = rt.materials.Emissive([1, 1, 1], 5)
sphere = rt.shapes.Sphere([0, 0, -2], 0.5, redMat)

groundMat = rt.materials.Diffuse([0.5, 0.5, 0.5])
ground = rt.shapes.Sphere([0, -100.5, -1], 100, groundMat)

camera = rt.Camera([0, 0, 0], 16/9, 90, 1)

renderer = rt.Renderer(540, samples_per_pixel=50, max_depth=10, background=[0, 0, 0], aspect_ratio=16/9) #0.5, 0.7, 1

renderer.add_shape(sphere)
renderer.add_shape(ground)

renderer.render(camera)