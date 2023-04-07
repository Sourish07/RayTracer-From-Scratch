#include "rectangle.h"

RectangleXY::RectangleXY(const double x0, const double x1, const double y0,
                         const double y1, const double z,
                         const std::shared_ptr<Material> &material, bool flipNormal)
    : Shape(material), x0(x0), x1(x1), y0(y0), y1(y1), z(z), flipNormal(flipNormal) {}

double RectangleXY::hit(const Ray &ray) const {
    double t = (z - ray.origin.z) / ray.direction.z;
    if (t < 1e-3) {
        return -1;
    }
    double x = ray.origin.x + t * ray.direction.x;
    double y = ray.origin.y + t * ray.direction.y;
    if (x < x0 || x > x1 || y < y0 || y > y1) {
        return -1;
    }

    // check if direction of ray and normal of rectangle are in the same direction
    // if (ray.direction.z * (flipNormal ? -1 : 1) < 0) {
    //     return -1;
    // }
    return t;
}

Vector RectangleXY::normalAt(const Vector &p) const { return Vector(0, 0, flipNormal ? -1 : 1); }

RectangleXZ::RectangleXZ(const double x0, const double x1, const double z0,
                         const double z1, const double y,
                         const std::shared_ptr<Material> &material, bool flipNormal)
    : Shape(material), x0(x0), x1(x1), z0(z0), z1(z1), y(y), flipNormal(flipNormal) {}

double RectangleXZ::hit(const Ray &ray) const {
    double t = (y - ray.origin.y) / ray.direction.y;
    if (t < 1e-3) {
        return -1;
    }
    double x = ray.origin.x + t * ray.direction.x;
    double z = ray.origin.z + t * ray.direction.z;
    if (x < x0 || x > x1 || z < z0 || z > z1) {
        return -1;
    }
    // check if direction of ray and normal of rectangle are in the same direction
    // if (ray.direction.y * (flipNormal ? -1 : 1) < 0) {
    //     return -1;
    // }

    return t;
}

Vector RectangleXZ::normalAt(const Vector &p) const { return Vector(0, flipNormal ? -1 : 1, 0); }

RectangleYZ::RectangleYZ(const double y0, const double y1, const double z0,
                         const double z1, const double x,
                         const std::shared_ptr<Material> &material, bool flipNormal)
    : Shape(material), y0(y0), y1(y1), z0(z0), z1(z1), x(x), flipNormal(flipNormal) {}

double RectangleYZ::hit(const Ray &ray) const {
    double t = (x - ray.origin.x) / ray.direction.x;
    if (t < 1e-3) {
        return -1;
    }
    double y = ray.origin.y + t * ray.direction.y;
    double z = ray.origin.z + t * ray.direction.z;
    if (y < y0 || y > y1 || z < z0 || z > z1) {
        return -1;
    }

    // check if direction of ray and normal of rectangle are in the same direction
    // if (ray.direction.x * (flipNormal ? -1 : 1) < 0) {
    //     return -1;
    // }
    return t;
}

Vector RectangleYZ::normalAt(const Vector &p) const { return Vector(flipNormal ? -1 : 1, 0, 0); }