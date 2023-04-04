#include "vector.h"

Vector::Vector(double x, double y, double z) : x(x), y(y), z(z) {}

Vector Vector::operator+(const Vector &other) const {
    return Vector(x + other.x, y + other.y, z + other.z);
}

Vector &Vector::operator+=(const Vector &other) {
    x += other.x;
    y += other.y;
    z += other.z;
    return *this;
}

Vector Vector::operator-(const Vector &other) const { return *this + (-other); }

Vector &Vector::operator-=(const Vector &other) {
    *this += (-other);
    return *this;
}

Vector Vector::operator-() const { return Vector(-x, -y, -z); }

Vector Vector::operator*(const Vector &other) const {
    return Vector(x * other.x, y * other.y, z * other.z);
}

Vector Vector::operator*(double scalar) const {
    return Vector(x * scalar, y * scalar, z * scalar);
}

Vector &Vector::operator*=(const Vector &other) {
    x *= other.x;
    y *= other.y;
    z *= other.z;
    return *this;
}

Vector &Vector::operator*=(double scalar) {
    x *= scalar;
    y *= scalar;
    z *= scalar;
    return *this;
}

Vector Vector::operator/(const Vector &other) const {
    return Vector(x / other.x, y / other.y, z / other.z);
}

Vector Vector::operator/(double scalar) const {
    return Vector(x / scalar, y / scalar, z / scalar);
}

Vector &Vector::operator/=(const Vector &other) {
    x /= other.x;
    y /= other.y;
    z /= other.z;
    return *this;
}

Vector &Vector::operator/=(double scalar) {
    x /= scalar;
    y /= scalar;
    z /= scalar;
    return *this;
}

double Vector::length() const { return std::sqrt(lengthSquared()); }

double Vector::lengthSquared() const { return x * x + y * y + z * z; }

Vector Vector::normalize() const { return *this / length(); }

double Vector::dot(const Vector &other) const {
    return x * other.x + y * other.y + z * other.z;
}

bool Vector::nearZero() const {
    const double s = 1e-6;
    return std::abs(x) < s && std::abs(y) < s && std::abs(z) < s;
}

std::ostream& operator<<(std::ostream &os, const Vector &v) {
    os << "[" << v.x << ", " << v.y << ", " << v.z << "]";
    return os;
}

Vector Vector::random() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dist(0, 1);
    return Vector(dist(gen), dist(gen), dist(gen));
}

Vector Vector::random(double min, double max) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dist(min, max);
    return Vector(dist(gen), dist(gen), dist(gen));
}

Vector Vector::randomInUnitSphere() {
    while (true) {
        Vector p = random(-1, 1);
        if (p.lengthSquared() >= 1) {
            continue;
        }
        return p;
    }
}

Vector Vector::randomUnitVector() {
    return randomInUnitSphere().normalize();
}