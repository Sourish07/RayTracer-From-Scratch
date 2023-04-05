#include "glass.h"

Glass::Glass(const Vector &color, const double ior)
    : Material(color), ior(ior) {}

Ray Glass::bounce(const Ray &r, const Vector &normal,
                  const Vector &hitPos) const {
    auto outside = r.direction.dot(normal) < 0;
    auto refractionRatio = outside ? 1.0 / ior : ior;

    auto _normal = outside ? normal : -normal;

    auto unitDirection = r.direction.normalize();
    auto cosTheta = fmin(-unitDirection.dot(_normal), 1.0);
    auto sinTheta = sqrt(1.0 - cosTheta * cosTheta);

    auto cannotRefract = refractionRatio * sinTheta > 1.0;
    double randomNum = random();
    auto newDirection =
        cannotRefract || reflectance(cosTheta, refractionRatio) > randomNum
            ? reflect(unitDirection, _normal)
            : refract(unitDirection, _normal, refractionRatio);

    return Ray(hitPos, newDirection);
}

Vector Glass::refract(const Vector &direction, const Vector &normal,
                      const double refractionRatio) {
    auto cosTheta = fmin(-direction.dot(normal), 1.0);
    Vector rOutPerp = refractionRatio * (direction + cosTheta * normal);
    Vector rOutParallel = -sqrt(fabs(1.0 - rOutPerp.lengthSquared())) * normal;
    return rOutPerp + rOutParallel;
}

Vector Glass::reflect(const Vector &direction, const Vector &normal) {
    return direction - 2 * direction.dot(normal) * normal;
}

double Glass::reflectance(double cosine, double refractionRatio) {
    auto r0 = (1 - refractionRatio) / (1 + refractionRatio);
    r0 = r0 * r0;
    return r0 + (1 - r0) * pow((1 - cosine), 5);
}