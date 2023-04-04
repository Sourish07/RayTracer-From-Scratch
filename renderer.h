#ifndef RENDERER_H
#define RENDERER_H

#include <memory>
#include <vector>
#include "ray.h"
#include "shapes/shape.h"
#include "camera.h"

class Renderer {
    public:
        Renderer(int imageHeight,  int samplesPerPixel, int maxDepth, Vector background, float aspectRatio);
        Vector rayColor(Ray &r) const;
        void addShape(std::shared_ptr<Shape> shape);
        void render(Camera &camera) const;

    public:
        int imageHeight;
        int imageWidth;
        int samplesPerPixel;
        int maxDepth;
        Vector background;
        float aspectRatio;
        std::vector<std::shared_ptr<Shape>> shapes;
};

#endif