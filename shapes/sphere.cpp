#include "sphere.h"

Sphere::Sphere(const Vector &center, const double radius,
               const std::shared_ptr<Material> &material)
    : Shape(material), center(center), radius(radius) {}

double Sphere::hit(const Ray &r) const {
    Vector oc = r.origin - center;
    double a = r.direction.dot(r.direction);
    double half_b = oc.dot(r.direction);
    double c = oc.dot(oc) - radius * radius;
    double discriminant = half_b * half_b - a * c;

    if (discriminant > 0) {
        double sqrt_discriminant = sqrt(discriminant);
        double t = (-half_b - sqrt_discriminant) / a;
        if (t > 1e-3) {
            return t;
        }
        t = (-half_b + sqrt_discriminant) / a;
        if (t > 1e-3) {
            return t;
        }
    }
    return -1;
}

Vector Sphere::normalAt(const Vector &p) const {
    return (p - center).normalize();
}