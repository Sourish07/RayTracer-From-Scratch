#include "diffuse.h"

Diffuse::Diffuse(const Vector &color) : Material(color) {}

Ray Diffuse::bounce(const Ray &r, const Vector &normal,
                    const Vector &hitPos) const {
    Vector newDirection = normal + Vector::randomUnitVector();
    if (newDirection.nearZero()) {
        newDirection = normal;
    }
    return Ray(hitPos, newDirection);
}