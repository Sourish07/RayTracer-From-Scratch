#include "materials/diffuse.h"
#include "renderer.h"
#include "shapes/sphere.h"
#include "vector.h"
#include <iostream>
#include <memory>

int main() {
    auto redMat = std::make_shared<Diffuse>(Vector(1, 0, 0));
    auto sphere = std::make_shared<Sphere>(Vector(0, 0, -2), 0.5, redMat);

    auto groundMat = std::make_shared<Diffuse>(Vector(0.5, 1, 0.5));
    auto floorSphere = std::make_shared<Sphere>(Vector(0, -100.5, -1), 100, groundMat);

    Camera c(Vector(0, 0, 0), 16./9, 90, 1);
    Renderer r = Renderer(720, 25, 10, Vector(0.5, 0.7, 1.0), 16./9);
    r.addShape(sphere);
    r.addShape(floorSphere);
    r.render(c);

    return 0;
}