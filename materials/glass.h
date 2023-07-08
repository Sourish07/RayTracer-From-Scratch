#ifndef GLASS_H
#define GLASS_H

#include "material.h"

class Glass : public Material {
    public:
        Glass(const Vector &color, const double ior);
        Ray bounce(const Ray &r, const Vector &normal, const Vector &hitPos) const override;
        static Vector refract(const Vector &direction, const Vector &normal, const double refractionRatio);
        static Vector reflect(const Vector &direction, const Vector &normal);
        static double reflectance(double cosine, double refractionRatio);

    public:
        double ior;
};

#endif