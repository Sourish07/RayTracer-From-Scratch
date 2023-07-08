#ifndef MATERIAL_H
#define MATERIAL_H

#include "../ray.h"

class Material {
    public:
        Material(const Vector &color);
        virtual Ray bounce(const Ray &r, const Vector &normal, const Vector &hitPos) const = 0;
        Vector emitted() const;
    
    public:
        Vector color;
};

#endif