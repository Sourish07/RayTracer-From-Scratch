#include <iostream>
#include "vector.h"

int main() {
    Vector v1(1, 2, 3);
    Vector v2(4, 5, 6);
    Vector v3 = v1 + v2;
    std::cout << "v1: " << v1 << std::endl;
    std::cout << "v2: " << v2 << std::endl;
    std::cout << "v3: " << v3 << std::endl;
}