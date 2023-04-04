#ifndef SHAPE_H
#define SHAPE_H

#include "../ray.h"
#include "../materials/material.h"

class Shape {
    public:
        Shape(const std::shared_ptr<Material>& material) : material(material) {};
        virtual double hit(Ray &r) const = 0;
        virtual Vector normalAt(Vector &p) const = 0;

    public:
        std::shared_ptr<Material> material;
};

#endif