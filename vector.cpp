#include "vector.h"

std::mt19937 Vector::gen([]() {
    std::random_device rd;
    return rd();
}());
std::uniform_real_distribution<double> Vector::uniDist(0.0, 1.0);
std::normal_distribution<double> Vector::normDist(0.0, 1.0);

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

std::ostream &operator<<(std::ostream &os, const Vector &v) {
    os << "[" << v.x << ", " << v.y << ", " << v.z << "]";
    return os;
}

Vector Vector::random() {
    std::mt19937 gen;
    std::uniform_real_distribution<double> dist(0.0, 1.0);
    return Vector(dist(gen), dist(gen), dist(gen));
}

Vector Vector::random(double min, double max) {
    static std::uniform_real_distribution<double> distribution(min, max);
    static std::mt19937 generator;
    return Vector( distribution(generator),  distribution(generator),  distribution(generator));
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
    double x = normDist(gen);
    double y = normDist(gen);
    double z = normDist(gen);
    if (x == 0 && y == 0 && z == 0)
    {
        return Vector(0, 1, 0);
    }
    return Vector(x, y, z) / std::sqrt(x * x + y * y + z * z);
}

Vector operator*(double scalar, const Vector &v) { return v * scalar; }

Vector Vector::randomCosWeighted() {
    double u = uniDist(gen);
    double v = uniDist(gen);

    double radial = std::sqrt(u);
    double theta = 2 * M_PI * v;

    return Vector(radial * std::cos(theta), radial * std::sin(theta), std::sqrt(1 - u));
}

Vector Vector::cross(const Vector &other) const {
    return Vector(y * other.z - z * other.y, 
                  z * other.x - x * other.z,
                  x * other.y - y * other.x);
}