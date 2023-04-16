#include "metal.h"

#include "../ray.h"

Metal::Metal(const Vector &color, float fuzz) : Material(color), fuzz(fuzz) {}

Ray Metal::bounce(const Ray &r, const Vector &normal, const Vector &hitPos) const {
    Vector reflected = r.direction.normalize() - 2 * r.direction.normalize().dot(normal) * normal;
    if (fuzz == 0)
    {
        return Ray(hitPos, reflected);
    }
    
    return Ray(hitPos, reflected + fuzz * Vector::randomInUnitSphere());
}