import raytracer as rt

redMat = rt.materials.Diffuse([1, 0, 0])
sphere = rt.shapes.Sphere([0, 0, -2], 0.5, redMat)

groundMat = rt.materials.Diffuse([0.5, 1, 0.5])
ground = rt.shapes.Sphere([0, -100.5, -1], 100, groundMat)

camera = rt.Camera([0, 0, 0], 16/9, 90, 1)

renderer = rt.Renderer(720, samples_per_pixel=25, max_depth=10, background=[0.5, 0.7, 1], aspect_ratio=16/9)

renderer.add_shape(sphere)
renderer.add_shape(ground)

renderer.render(camera)