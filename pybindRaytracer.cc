#include <pybind11/pybind11.h>

#include "camera.h"
#include "renderer.h"
#include "vector.h"

#include "materials/diffuse.h"
#include "materials/emissive.h"
#include "materials/glass.h"
#include "materials/material.h"
#include "materials/metal.h"

#include "shapes/cube.h"
#include "shapes/disc.h"
#include "shapes/plane.h"
#include "shapes/rectangle.h"
#include "shapes/shape.h"
#include "shapes/sphere.h"

namespace py = pybind11;

PYBIND11_MODULE(raytracer, m) {
    m.doc() = "Raytracer";

    py::class_<Renderer>(m, "Renderer")
        .def(py::init([](int image_height, int samples_per_pixel, int max_depth,
                         const py::list &background_list, double aspect_ratio) {
                 return std::make_unique<Renderer>(
                     image_height, samples_per_pixel, max_depth,
                     Vector(background_list[0].cast<double>(),
                            background_list[1].cast<double>(),
                            background_list[2].cast<double>()),
                     aspect_ratio);
             }),
             py::arg("image_height"), py::arg("samples_per_pixel"),
             py::arg("max_depth"), py::arg("background"),
             py::arg("aspect_ratio"))
        .def("add_shape", &Renderer::addShape, py::arg("shape"))
        .def("render", &Renderer::render, py::arg("cam"),
             py::arg("output_filename"));

    py::class_<Camera>(m, "Camera")
        .def(py::init([](const py::list &origin_list, double aspect_ratio,
                         double fov, double focal_length) {
                 return std::make_unique<Camera>(
                     Vector(origin_list[0].cast<double>(),
                            origin_list[1].cast<double>(),
                            origin_list[2].cast<double>()),
                     aspect_ratio, fov, focal_length);
             }),
             py::arg("origin"), py::arg("aspect_ratio"), py::arg("fov"),
             py::arg("focal_length"));

    py::module shapesModule = m.def_submodule("shapes", "Shapes submodule");

    py::class_<Shape, std::shared_ptr<Shape>>(shapesModule, "_Shape");

    py::class_<Sphere, std::shared_ptr<Sphere>, Shape>(shapesModule, "Sphere")
        .def(py::init([](const py::list center, double radius,
                         std::shared_ptr<Material> mat) {
                 return std::make_unique<Sphere>(
                     Vector(center[0].cast<double>(), center[1].cast<double>(),
                            center[2].cast<double>()),
                     radius, mat);
             }),
             py::arg("center"), py::arg("radius"), py::arg("material"));

    py::class_<Cube, std::shared_ptr<Cube>, Shape>(shapesModule, "Cube")
        .def(py::init([](const py::list center, double radius,
                         std::shared_ptr<Material> mat) {
                 return std::make_unique<Cube>(Vector(center[0].cast<double>(),
                                                      center[1].cast<double>(),
                                                      center[2].cast<double>()),
                                               radius, mat);
             }),
             py::arg("center"), py::arg("radius"), py::arg("material"));

    py::class_<RectangleXY, std::shared_ptr<RectangleXY>, Shape>(shapesModule,
                                                                 "RectangleXY")
        .def(py::init([](double x0, double x1, double y0, double y1, double z,
                         std::shared_ptr<Material> mat, bool flipNormal) {
                 return std::make_unique<RectangleXY>(x0, x1, y0, y1, z, mat,
                                                      flipNormal);
             }),
             py::arg("x0"), py::arg("x1"), py::arg("y0"), py::arg("y1"),
             py::arg("radius"), py::arg("material"),
             py::arg("flipNormal") = false);

    py::class_<RectangleXZ, std::shared_ptr<RectangleXZ>, Shape>(shapesModule,
                                                                 "RectangleXZ")
        .def(py::init([](double x0, double x1, double y0, double y1, double z,
                         std::shared_ptr<Material> mat, bool flipNormal) {
                 return std::make_unique<RectangleXZ>(x0, x1, y0, y1, z, mat,
                                                      flipNormal);
             }),
             py::arg("x0"), py::arg("x1"), py::arg("y0"), py::arg("y1"),
             py::arg("radius"), py::arg("material"),
             py::arg("flipNormal") = false);

    py::class_<RectangleYZ, std::shared_ptr<RectangleYZ>, Shape>(shapesModule,
                                                                 "RectangleYZ")
        .def(py::init([](double y0, double y1, double z0, double z1, double x,
                         std::shared_ptr<Material> mat, bool flipNormal) {
                 return std::make_unique<RectangleYZ>(y0, y1, z0, z1, x, mat,
                                                      flipNormal);
             }),
             py::arg("y0"), py::arg("y1"), py::arg("z0"), py::arg("z1"),
             py::arg("radius"), py::arg("material"),
             py::arg("flipNormal") = false);

    py::class_<Plane, std::shared_ptr<Plane>, Shape>(shapesModule, "Plane")
        .def(py::init([](const py::list normal, const py::list point,
                         const py::list color, std::shared_ptr<Material> mat) {
                 return std::make_unique<Plane>(
                     Vector(normal[0].cast<double>(), normal[1].cast<double>(),
                            normal[2].cast<double>()),
                     Vector(point[0].cast<double>(), point[1].cast<double>(),
                            point[2].cast<double>()),
                     Vector(color[0].cast<double>(), color[1].cast<double>(),
                            color[2].cast<double>()),
                     mat);
             }),
             py::arg("normal"), py::arg("point"), py::arg("color"),
             py::arg("material"));

       py::class_<Disc, std::shared_ptr<Disc>, Shape>(shapesModule, "Disc")
        .def(py::init([](const py::list center, const py::list normal,
                         double radius, std::shared_ptr<Material> mat) {
                 return std::make_unique<Disc>(
                     Vector(center[0].cast<double>(), center[1].cast<double>(),
                            center[2].cast<double>()),
                     Vector(normal[0].cast<double>(), normal[1].cast<double>(),
                            normal[2].cast<double>()),
                     radius, mat);
             }),
             py::arg("center"), py::arg("normal"), py::arg("radius"),
             py::arg("material"));

    py::module materialsModule =
        m.def_submodule("materials", "Materials submodule");

    py::class_<Material, std::shared_ptr<Material>>(materialsModule,
                                                    "_Material");

    py::class_<Diffuse, std::shared_ptr<Diffuse>, Material>(materialsModule,
                                                            "Diffuse")
        .def(py::init([](const py::list color_list) {
                 return std::make_unique<Diffuse>(Vector(
                     color_list[0].cast<double>(), color_list[1].cast<double>(),
                     color_list[2].cast<double>()));
             }),
             py::arg("color"));

    py::class_<Emissive, std::shared_ptr<Emissive>, Material>(materialsModule,
                                                              "Emissive")
        .def(py::init([](const py::list color_list, double intensity) {
                 return std::make_unique<Emissive>(
                     Vector(color_list[0].cast<double>(),
                            color_list[1].cast<double>(),
                            color_list[2].cast<double>()),
                     intensity);
             }),
             py::arg("color"), py::arg("intensity"));

    py::class_<Glass, std::shared_ptr<Glass>, Material>(materialsModule,
                                                        "Glass")
        .def(py::init([](const py::list color_list, double ior) {
                 return std::make_unique<Glass>(
                     Vector(color_list[0].cast<double>(),
                            color_list[1].cast<double>(),
                            color_list[2].cast<double>()),
                     ior);
             }),
             py::arg("color"), py::arg("index_of_refraction"));

    py::class_<Metal, std::shared_ptr<Metal>, Material>(materialsModule,
                                                        "Metal")
        .def(py::init([](const py::list color_list, double fuzz) {
                 return std::make_unique<Metal>(
                     Vector(color_list[0].cast<double>(),
                            color_list[1].cast<double>(),
                            color_list[2].cast<double>()),
                     fuzz);
             }),
             py::arg("color"), py::arg("fuzz") = 0.0);
}