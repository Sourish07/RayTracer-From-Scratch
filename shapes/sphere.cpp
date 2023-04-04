#include "sphere.h"

Sphere::Sphere(const Vector &center, const double radius, const std::shared_ptr<Material>& material)
    : Shape(material), center(center), radius(radius) {}

double Sphere::hit(Ray &r) const {
    Vector oc = r.origin - center;
    double a = r.direction.dot(r.direction);
    double b = 2 * oc.dot(r.direction);
    double c = oc.dot(oc) - radius * radius;
    double discriminant = b * b - 4 * a * c;
    if (discriminant > 0) {
        double t = (-b - sqrt(discriminant)) / (2 * a);
        if (t > 1e-3) {
            return t;
        }
        t = (-b + sqrt(discriminant)) / (2 * a);
        if (t > 1e-3) {
            return t;
        }
    }
    return -1;
}

Vector Sphere::normalAt(Vector &p) const { 
    return (p - center).normalize(); 
}