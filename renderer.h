#ifndef RENDERER_H
#define RENDERER_H

#include <memory>
#include <string>
#include <vector>
#include "ray.h"
#include "shapes/shape.h"
#include "camera.h"

class Renderer {
    public:
        Renderer(int imageHeight,  int samplesPerPixel, int maxDepth, Vector background, float aspectRatio);
        Vector rayColor(Ray &r, int depth) const;
        void addShape(std::shared_ptr<Shape> shape);
        void render(Camera &camera, std::string outputFilename) const;

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