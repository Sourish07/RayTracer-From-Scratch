#include "diffuse.h"

Diffuse::Diffuse(const Vector &color, const double roughness) : Material(color), roughness(roughness) {}

Ray Diffuse::bounce(const Ray &r, const Vector &normal, const Vector &hitPos) const {
    // Normalize is called in Ray constructor
    return Ray(hitPos, (normal + Vector::randomUnitVector() * roughness));
}