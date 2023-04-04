// #include <pybind11/pybind11.h>

// #include "shapes/sphere.h"

// namespace py = pybind11;

// PYBIND11_MODULE(raytracer, m) {
//     m.doc() = "Raytracer";

//     py::class_<renderer>(m, "renderer")
//         .def(py::init<>())
//         .def(py::init([](int image_height, int samples_per_pixel, int max_depth,
//                          const py::list &background_list = [ 0.5, 0.7, 1.0 ],
//                          float aspect_ratio = 16 / 9) {
//                  return std::make_unique<renderer>(
//                      image_height, samples_per_pixel, max_depth,
//                      Vector(background_list[0].cast<float>(),
//                             background_list[1].cast<float>(),
//                             background_list[2].cast<float>()),
//                      aspect_ratio);
//              }),
//              py::arg("image_height"), py::arg("samples_per_pixel"),
//              py::arg("max_depth"), py::arg("background"),
//              py::arg("aspect_ratio"))
//         .def("add_shape", &renderer::addShape, py::arg("shape"))
//         .def("render", &renderer::render, py::arg("cam"))

//             py::module shapesModule =
//         m.def_submodule("shapes", "Shapes submodule");

//     py::class_<sphere, std::shared_ptr<sphere>, hittable>(shapesModule,
//                                                           "Sphere")
//         .def(py::init<point3, double, std::shared_ptr<material>>())
//         .def(
//             py::init([](py::list cen, double r, std::shared_ptr<material> mat) {
//                 return std::make_unique<sphere>(point3(cen[0].cast<double>(),
//                                                        cen[1].cast<double>(),
//                                                        cen[2].cast<double>()),
//                                                 r, mat);
//             }));
// }