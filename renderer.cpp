#include "renderer.h"

#include <iostream>
#include "materials/emissive.h"

Renderer::Renderer(int imageHeight, int samplesPerPixel, int maxDepth,
                   Vector background, float aspectRatio)
    : imageHeight(imageHeight), samplesPerPixel(samplesPerPixel),
      maxDepth(maxDepth), background(background), aspectRatio(aspectRatio) {
    imageWidth = aspectRatio * imageHeight;
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

    Vector emitted = hitShape->material->emitted();
    if (std::dynamic_pointer_cast<Emissive>(hitShape->material) != nullptr) {
        // cast hitShape material to Emissive
        emitted = std::dynamic_pointer_cast<Emissive>(hitShape->material)->emitted();
        return emitted;
    }

    Vector hitPos = r(t);
    Vector normal = hitShape->normalAt(hitPos);
    Vector color = hitShape->material->color;

    Ray bounceRay = hitShape->material->bounce(r, normal, hitPos);
    return emitted + color * rayColor(bounceRay, depth - 1);
}

// Vector Renderer::rayColor(Ray &r) const {
//     Vector color = Vector(1, 1, 1);
//     Ray currentRay = r;
//     for (int i = 0; i < maxDepth; i++) {
//         double t = INFINITY;
//         Vector normal;
//         Vector hitPos;
//         std::shared_ptr<Shape> hitShape = nullptr;

//         for (auto shape : shapes) {
//             double currentT = shape->hit(currentRay);
//             if (currentT > 0 && currentT < t) {
//                 t = currentT;
//                 hitShape = shape;
//             }
//         }
//         if (hitShape == nullptr) {
//             return color * background;
//         }

//         // Check if material of hit shape is emissive
//         bool isEmissive = std::dynamic_pointer_cast<Emissive>(hitShape->material) != nullptr;

//         hitPos = currentRay(t);
//         normal = hitShape->normalAt(hitPos);
//         Vector c = hitShape->material->color;
//         currentRay = hitShape->material->bounce(currentRay, normal, hitPos);
//         color *= hitShape->material->emitted() + hitShape->material->color;
//     }
//     return color;
// }

void Renderer::addShape(std::shared_ptr<Shape> shape) { shapes.push_back(shape); }

void Renderer::render(Camera &camera) const {
    std::cout << "P3\n" << imageWidth << " " << imageHeight << "\n255\n";

    for (int j = imageHeight - 1; j >= 0; j--) {
        std::cerr << "\rScanlines remaining: " << j << " " << std::flush;
        for (int i = 0; i < imageWidth; i++) {
            Vector color = Vector(0, 0, 0);
            for (int s = 0; s < samplesPerPixel; s++) {
                double r1 = rand() / (RAND_MAX + 1.0);
                double r2 = rand() / (RAND_MAX + 1.0);

                double u = (i + r1) / (imageWidth - 1);
                double v = (j + r2) / (imageHeight - 1);
                Ray r = camera.getRay(u, v);
                color += rayColor(r, maxDepth);
            }
            color /= samplesPerPixel;
            color = Vector(sqrt(color.x), sqrt(color.y), sqrt(color.z));
            int ir = static_cast<int>(255.999 * color.x);
            int ig = static_cast<int>(255.999 * color.y);
            int ib = static_cast<int>(255.999 * color.z);
            std::cout << ir << " " << ig << " " << ib << "\n";
        }
    }
    std::cerr << "\nDone.\n";
}