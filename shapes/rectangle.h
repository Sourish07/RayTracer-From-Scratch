#ifndef RECTANGLE_H
#define RECTANGLE_H

#include "shape.h"
#include <memory>

class RectangleXY : public Shape {
  public:
    RectangleXY(const double x0, const double x1, const double y0,
                const double y1, const double z,
                const std::shared_ptr<Material> &material, bool flipNormal);

    double hit(const Ray &ray) const override;
    Vector normalAt(const Vector &p) const override;

  public:
    double x0, x1, y0, y1;
    double z;
    std::shared_ptr<Material> material;
    bool flipNormal;
};

class RectangleXZ : public Shape {
  public:
    RectangleXZ(const double x0, const double x1, const double z0,
                const double z1, const double y,
                const std::shared_ptr<Material> &material, bool flipNormal);

    double hit(const Ray &ray) const override;
    Vector normalAt(const Vector &p) const override;

  public:
    double x0, x1, z0, z1;
    double y;
    std::shared_ptr<Material> material;
    bool flipNormal;
};

class RectangleYZ : public Shape {
  public:
    RectangleYZ(const double y0, const double y1, const double z0,
                const double z1, const double x,
                const std::shared_ptr<Material> &material, bool flipNormal);

    double hit(const Ray &ray) const override;
    Vector normalAt(const Vector &p) const override;

  public:
    double y0, y1, z0, z1;
    double x;
    std::shared_ptr<Material> material;
    bool flipNormal;
};

#endif