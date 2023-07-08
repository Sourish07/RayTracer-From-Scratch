#ifndef DISC_H
#define DISC_H

#include "shape.h"

class Disc : public Shape {
    public:
        Disc(const Vector &center, const Vector &normal, const double radius, const std::shared_ptr<Material> material);
        double hit(const Ray &ray) const override;
        Vector normalAt(const Vector &p) const override;

    public:
        Vector center;
        Vector normal;
        double radius;
};

#endif