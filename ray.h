#ifndef RAY_H
#define RAY_H

#include "vector.h"

class Ray {
    public:
        Ray(const Vector &origin, const Vector &direction);
        Vector at(double t) const;
        Vector operator()(double t) const;
        

    public:
        Vector origin;
        Vector direction;
};

#endif