#include "ray.h"

Ray::Ray(const Vector &origin, const Vector &direction) : origin(origin), direction(direction) {
    direction.normalize();
}

Vector Ray::at(double t) const {
    return origin + direction * t;
}

Vector Ray::operator()(double t) const {
    return at(t);
}