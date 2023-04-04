#ifndef VECTOR_H
#define VECTOR_H

#include <cmath>
#include <iostream>
#include <random>

class Vector
{
public:
    Vector(double x = 0.0, double y = 0.0, double z = 0.0);
    Vector operator+(const Vector &other) const;
    Vector &operator+=(const Vector &other);
    Vector operator-(const Vector &other) const;
    Vector &operator-=(const Vector &other);
    Vector operator-() const;
    Vector operator*(const Vector &other) const;
    Vector operator*(double scalar) const;
    Vector &operator*=(const Vector &other);
    Vector &operator*=(double scalar);
    Vector operator/(const Vector &other) const;
    Vector operator/(double scalar) const;
    Vector &operator/=(const Vector &other);
    Vector &operator/=(double scalar);

    double length() const;
    double length_squared() const;
    Vector normalize() const;
    double dot(const Vector &other) const;
    bool near_zero() const;

    friend std::ostream &operator<<(std::ostream &os, const Vector &v);

    static Vector random();
    static Vector random(double min, double max);
    static Vector random_in_unit_sphere();
    static Vector random_unit_vector();

private:
    double x, y, z;
};

#endif
