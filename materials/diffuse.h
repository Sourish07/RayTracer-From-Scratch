#ifndef DIFFUSE_H
#define DIFFUSE_H

#include "material.h"

class Diffuse : public Material {
    public:
        Diffuse(const Vector &color, const double roughness);
        Ray bounce(const Ray &r, const Vector &normal, const Vector &hitPos) const override;

    public:
        double roughness;
};

#endif