#include "plane.h"

Plane::Plane(const Vector &point, const Vector &normal,
             const std::shared_ptr<Material>& material)
    : Shape(material), point(point), normal(normal) {
}

double Plane::hit(const Ray &ray) const {
    double denom = ray.direction.dot(normal);
    if (denom > 1e-6) {
        Vector p0l0 = point - ray.origin;
        auto t = p0l0.dot(normal) / denom;
        return t;
    }
    return -1;
}

Vector Plane::normalAt(const Vector &p) const {
    return normal;
}