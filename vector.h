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
    double lengthSquared() const;
    Vector normalize() const;
    double dot(const Vector &other) const;
    bool nearZero() const;


    static Vector random();
    static Vector random(double min, double max);
    static Vector randomInUnitSphere();
    static Vector randomUnitVector();

public:
    double x, y, z;
};

std::ostream& operator<<(std::ostream& os, const Vector& v);
Vector operator*(double scalar, const Vector& v);

#endif
