#ifndef PLANE_H
#define PLANE_H

#include <memory>
#include "shape.h"

class Plane : public Shape {
    public:
        Plane(const Vector &normal, const Vector &point, const Vector &color, const std::shared_ptr<Material>& material);
        double hit(const Ray &ray) const;
        Vector normalAt(const Vector &p) const;

    public:
        Vector normal;
        Vector point;
};

#endif