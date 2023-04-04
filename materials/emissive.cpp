#include "emissive.h"

Emissive::Emissive(const Vector &color, const double intensity)
    : Material(color), intensity(intensity) {}

Ray Emissive::bounce(const Ray &r, const Vector &normal,
                     const Vector &hitPos) const {
    return Ray(Vector(), Vector());
}

Vector Emissive::emitted() const {
    return color * intensity;
}