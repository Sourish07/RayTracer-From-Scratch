#ifndef SPHERE_H
#define SPHERE_H

#include <memory>
#include "shape.h"

class Sphere : public Shape {
    public:
        Sphere(const Vector &center, const double radius, const std::shared_ptr<Material>& material);
        double hit(Ray &r) const override;
        Vector normalAt(Vector &p) const override;

    private:
        Vector center;
        double radius;
        
};

#endif