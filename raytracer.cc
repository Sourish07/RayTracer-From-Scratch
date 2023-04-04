#include <pybind11/pybind11.h>

#include "camera.h"
#include "renderer.h"
#include "vector.h"

#include "materials/material.h"
#include "materials/diffuse.h"
#include "materials/emissive.h"

#include "shapes/shape.h"
#include "shapes/sphere.h"

namespace py = pybind11;

PYBIND11_MODULE(raytracer, m) {
    m.doc() = "Raytracer";

    py::class_<Renderer>(m, "Renderer")
        .def(py::init([](int image_height, int samples_per_pixel, int max_depth,
                         const py::list &background_list, float aspect_ratio) {
                 return std::make_unique<Renderer>(
                     image_height, samples_per_pixel, max_depth,
                     Vector(background_list[0].cast<float>(),
                            background_list[1].cast<float>(),
                            background_list[2].cast<float>()),
                     aspect_ratio);
             }),
             py::arg("image_height"), py::arg("samples_per_pixel"),
             py::arg("max_depth"), py::arg("background"),
             py::arg("aspect_ratio"))
        .def("add_shape", &Renderer::addShape, py::arg("shape"))
        .def("render", &Renderer::render, py::arg("cam"));

    py::class_<Camera>(m, "Camera")
        .def(py::init([](const py::list &origin_list, float aspect_ratio,
                         float fov, float focal_length) {
                 return std::make_unique<Camera>(
                     Vector(origin_list[0].cast<float>(),
                            origin_list[1].cast<float>(),
                            origin_list[2].cast<float>()),
                     aspect_ratio, fov, focal_length);
             }),
             py::arg("origin"), py::arg("aspect_ratio"), py::arg("fov"),
             py::arg("focal_length"));

    
    
    py::module shapesModule = m.def_submodule("shapes", "Shapes submodule");

    py::class_<Shape, std::shared_ptr<Shape>>(shapesModule, "_Shape");

    py::class_<Sphere, std::shared_ptr<Sphere>, Shape>(shapesModule, "Sphere")
        .def(py::init([](const py::list center, double radius, std::shared_ptr<Material> mat) {
                 return std::make_unique<Sphere>(
                     Vector(center[0].cast<float>(), center[1].cast<float>(),
                            center[2].cast<float>()),
                     radius, mat);
             }),
             py::arg("center"), py::arg("radius"), py::arg("material"));



    py::module materialsModule = m.def_submodule("materials", "Materials submodule");

    py::class_<Material, std::shared_ptr<Material>>(materialsModule, "_Material");

    py::class_<Diffuse, std::shared_ptr<Diffuse>, Material>(materialsModule, "Diffuse")
        .def(py::init([](const py::list color_list) {
                 return std::make_unique<Diffuse>(
                     Vector(color_list[0].cast<float>(), color_list[1].cast<float>(),
                            color_list[2].cast<float>()));
             }),
             py::arg("color"));

    py::class_<Emissive, std::shared_ptr<Emissive>, Material>(materialsModule, "Emissive")
        .def(py::init([](const py::list color_list, double intensity) {
                 return std::make_unique<Emissive>(
                     Vector(color_list[0].cast<float>(), color_list[1].cast<float>(),
                            color_list[2].cast<float>()), intensity);
             }),
             py::arg("color"), py::arg("intensity"));
}