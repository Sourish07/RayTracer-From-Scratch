#ifndef DIFFUSE_H
#define DIFFUSE_H

#include "material.h"

class Diffuse : public Material {
    public:
        Diffuse(const Vector &color);
        Ray bounce(const Ray &r, const Vector &normal, const Vector &hitPos) const override;
};

#endif