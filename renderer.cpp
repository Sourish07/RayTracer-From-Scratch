#include <iostream>

#ifdef USE_OPENMP
#include <omp.h>
#endif

#include "materials/emissive.h"
#include "renderer.h"

Renderer::Renderer(int imageHeight, int samplesPerPixel, int maxDepth,
                   Vector background, float aspectRatio)
    : imageHeight(imageHeight),
      samplesPerPixel(samplesPerPixel),
      maxDepth(maxDepth),
      background(background),
      aspectRatio(aspectRatio) {
    imageWidth = (int)(aspectRatio * imageHeight);
}

Vector Renderer::rayColor(Ray &r, int depth) const {
    if (depth <= 0) {
        return Vector(0, 0, 0);
    }

    double t = INFINITY;
    Shape *hitShape = nullptr;

    for (auto shape : shapes) {
        double currentT = shape->hit(r);
        if (currentT > 0 && currentT < t) {
            t = currentT;
            hitShape = shape.get();
        }
    }

    if (hitShape == nullptr) {
        return background;
    }

    if (std::dynamic_pointer_cast<Emissive>(hitShape->material) !=
        nullptr) {  // Checking if hitShape material is Emissive
        // cast hitShape material to Emissive
        return std::dynamic_pointer_cast<Emissive>(hitShape->material)
            ->emitted();
    }

    Vector hitPos = r(t);
    Vector normal = hitShape->normalAt(hitPos);
    Vector color = hitShape->material->color;

    Ray bounceRay = hitShape->material->bounce(r, normal, hitPos);
    return color * rayColor(bounceRay, depth - 1);
}

void Renderer::addShape(std::shared_ptr<Shape> shape) {
    shapes.push_back(shape);
}

void Renderer::render(Camera &camera, std::string outputFilename) const {
    // Print the number of threads being used
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dist(-1, 1);

    Vector *buffer = new Vector[imageWidth * imageHeight];
#ifdef USE_OPENMP
    std::cout << "Number of threads: " << omp_get_max_threads() << std::endl;

#pragma omp parallel for schedule(dynamic, 1)
#endif
    for (int j = 0; j < imageHeight; j++) {
        fprintf(stderr, "\rRendering (%d spp) %5.2f%%", samplesPerPixel,
                100. * j / (imageHeight - 1));

        for (int i = 0; i < imageWidth; i++) {
            Vector color = Vector(0, 0, 0);
            for (int s = 0; s < samplesPerPixel; s++) {
                double u = (i + dist(gen)) / (imageWidth - 1);
                double v = (j + dist(gen)) / (imageHeight - 1);
                Ray camRay = camera.getRay(u, v);
                color += rayColor(camRay, maxDepth);
            }
            color =
                Vector(sqrt(color.x / samplesPerPixel),
                       sqrt(color.y / samplesPerPixel),
                       sqrt(color.z /
                            samplesPerPixel));  // gamma correction (gamma = 2)

            double ir = 255.999 * color.x;
            double ig = 255.999 * color.y;
            double ib = 255.999 * color.z;

            buffer[(imageHeight - j - 1) * imageWidth + i] +=
                Vector(ir, ig, ib);
        }
    }

    FILE *f = fopen(outputFilename.c_str(), "w");
    fprintf(f, "P3\n%d %d\n%d\n", imageWidth, imageHeight, 255);

    for (int i = 0; i < imageWidth * imageHeight; i++) {
        fprintf(f, "%d %d %d\n", (int)buffer[i].x, (int)buffer[i].y,
                (int)buffer[i].z);
    }

    fprintf(stderr, "\nDone!\n");
}