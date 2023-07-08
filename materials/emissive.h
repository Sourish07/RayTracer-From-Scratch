#ifndef EMISSIVE_H
#define EMISSIVE_H

#include "material.h"

class Emissive : public Material {
    public:
        Emissive(const Vector &color, const double intensity);
        Ray bounce(const Ray &r, const Vector &normal, const Vector &hitPos) const override;
        Vector emitted() const;

    public:
        double intensity;
};

#endif