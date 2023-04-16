#include "diffuse.h"

Diffuse::Diffuse(const Vector &color, const double roughness) : Material(color), roughness(roughness) {}

Ray Diffuse::bounce(const Ray &r, const Vector &normal, const Vector &hitPos) const {
    // Normalize is called in Ray constructor
    // Randomly choosing a point on a unit sphere and adding it to the normal scales with cosine(theta)
    return Ray(hitPos, (normal + Vector::randomUnitVector() * roughness));
}