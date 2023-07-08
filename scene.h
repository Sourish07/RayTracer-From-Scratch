#ifndef SCENE_H
#define SCENE_H

#include <vector>
#include "shapes/shape.h"

class Scene {
    public:
        Scene();
        void addShape(Shape *shape);
    
    public:
        std::vector<Shape *> shapes;
};

#endif
