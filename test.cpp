#include <iostream>
#include <memory>

#include "materials/diffuse.h"
#include "materials/emissive.h"
#include "renderer.h"
#include "shapes/sphere.h"
#include "vector.h"

int main() {
    Vector v1 = Vector::randomUnitVector();
    Vector v2 = Vector::randomUnitVector();
    Vector v3 = Vector::randomUnitVector();

    std::cout << v1 << std::endl;
    std::cout << v2 << std::endl;
    std::cout << v3 << std::endl;

    return 0;
}