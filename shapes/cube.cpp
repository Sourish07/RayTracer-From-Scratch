#include <algorithm>
#include "cube.h"

Cube::Cube(const Vector &center, const double radius,
           const std::shared_ptr<Material> &material)
    : Shape(material), center(center), radius(radius) {
    min = center - Vector(radius, radius, radius);
    max = center + Vector(radius, radius, radius);
}

double Cube::hit(const Ray &ray) const {
    Vector t0 = (min - ray.origin) / ray.direction;
    Vector t1 = (max - ray.origin) / ray.direction;

    double t_min = std::max({std::min(t0.x, t1.x), std::min(t0.y, t1.y), std::min(t0.z, t1.z)});
    double t_max = std::min({std::max(t0.x, t1.x), std::max(t0.y, t1.y), std::max(t0.z, t1.z)});

    if (t_min <= t_max) {
        if (t_min > 1e-3) {
            return t_min;
        } else if (t_max > 1e-3) {
            return t_max;
        }
    }
    return -1;
}

Vector Cube::normalAt(const Vector &pos) const {
    Vector adjusted_pos = pos - center;
    adjusted_pos = adjusted_pos.normalize();

    Vector dirs[] = {
        Vector(1, 0, 0), Vector(0, 1, 0), Vector(0, 0, 1),
        Vector(-1, 0, 0), Vector(0, -1, 0), Vector(0, 0, -1)
    };

    double max_dot = -1;
    Vector normal;

    for (const auto &dir : dirs) {
        double dot = adjusted_pos.dot(dir);
        if (dot > max_dot) {
            max_dot = dot;
            normal = dir;
        }
    }

    return normal;
}