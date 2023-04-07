#include "disc.h"

Disc::Disc(const Vector &center, const Vector &normal, const double radius,
           const std::shared_ptr<Material> material)
    : Shape(material), center(center), normal(normal), radius(radius) {}

double Disc::hit(const Ray &r) const {
    /**
     * The dot product of two vectors is zero if they are perpendicular. 
     * This means if the dot product of the ray direction and the NORMAL of the disc is zero, the ray is perpendicular to the disc's normal.
     * This in turn would mean the ray direction is parallel to the disc itself. (Normal of plane is perpendicular to plane)
     */
    double denom = normal.dot(r.direction);
    
    if (denom > 1e-6) {
        Vector oc = center - r.origin;
        double t = oc.dot(normal) / denom;
        if (t > 1e-3) {
            Vector p = r.origin + r.direction * t;
            if ((p - center).length() <= radius) {
                return t;
            }
        }
    }
    return -1;
}

Vector Disc::normalAt(const Vector &p) const { return normal; }