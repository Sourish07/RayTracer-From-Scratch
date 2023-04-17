#include "diffuse.h"

Diffuse::Diffuse(const Vector &color, const double roughness) : Material(color), roughness(roughness) {}

Ray Diffuse::bounce(const Ray &r, const Vector &normal, const Vector &hitPos) const {
    // Normalize is called in Ray constructor
    // Randomly choosing a point on a unit sphere and adding it to the normal scales with cosine(theta)
    
    Vector randCos = Vector::randomCosWeighted();
    Vector u;
    // Create orthonormal basis with normal being w vector
    if (fabs(normal.x) > 0.9) {
        u = normal.cross(Vector(0.0, 1.0, 0.0)).normalize();
    } else {
        u = normal.cross(Vector(1.0, 0.0, 0.0)).normalize();
    }
    Vector v = normal.cross(u).normalize();
    
    Vector randCosBasis = (u * randCos.x) + (v * randCos.y) + (normal * randCos.z);
    return Ray(hitPos, randCosBasis);
    

    //return Ray(hitPos, (normal + Vector::randomUnitVector() * roughness));
}