#include "material.h"

Material::Material(const Vector &color) : color(color) {}

Vector Material::emitted() const {
    return Vector(0, 0, 0);
}