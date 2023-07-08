#ifndef CUBE_H
#define CUBE_H

#include <memory>
#include "shape.h"

class Cube : public Shape {
  public:
    Cube(const Vector &center, const double radius,
         const std::shared_ptr<Material> &material);

    double hit(const Ray &ray) const override;
    Vector normalAt(const Vector &p) const override;

  public:
    Vector center;
    double radius;
    Vector min;
    Vector max;
};

#endif