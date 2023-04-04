#include "camera.h"

Camera::Camera(const Vector &origin, double aspectRatio, int fov,
               int focalLength)
    : origin(origin), aspectRatio(aspectRatio), fov(fov),
      focalLength(focalLength) {
    double theta = fov * M_PI / 180;
    double halfHeight = tan(theta / 2);
    double halfWidth = aspectRatio * halfHeight;
    viewportHeight = 2 * halfHeight;
    viewportWidth = 2 * halfWidth;
    horizontal = Vector(viewportWidth, 0, 0);
    vertical = Vector(0, viewportHeight, 0);
    lowerLeftCorner =
        origin - horizontal / 2 - vertical / 2 - Vector(0, 0, focalLength);
}

Ray Camera::getRay(double u, double v) const {
    return Ray(origin,
               lowerLeftCorner + horizontal * u + vertical * v - origin);
}