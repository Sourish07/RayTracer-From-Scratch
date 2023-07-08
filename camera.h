#ifndef CAMERA_H
#define CAMERA_H

#include "ray.h"

class Camera {
    public:
        Camera(const Vector &origin, double aspectRatio=16/9, int fov=60, int focalLength=1);
        Ray getRay(double x, double y) const;

    public:
        Vector origin;
        double aspectRatio;
        int focalLength;
        int fov;
        double viewportHeight;
        double viewportWidth;
        Vector horizontal;
        Vector vertical;
        Vector lowerLeftCorner;
};

#endif