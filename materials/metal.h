#ifndef METAL_H
#define METAL_H

// #include "../ray.h"
#include "material.h"

class Metal : public Material {
    public:
        Metal(const Vector &color, float fuzz);
        Ray bounce(const Ray &r, const Vector &normal, const Vector &hitPos) const;
    
    public:
        float fuzz;
};

#endif