cmake_minimum_required(VERSION 3.0.0)
project(raytracer VERSION 0.1.0)

# add_executable(main test.cpp vector.cpp)

execute_process (
    COMMAND python3 -c "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE PYBIND11_DIR
)

string(STRIP ${PYBIND11_DIR} PYBIND11_DIR)

# set(pybind11_DIR /home/sourish/.local/lib/python3.8/site-packages/pybind11/share/cmake/pybind11)
set(pybind11_DIR ${PYBIND11_DIR})

find_package(pybind11 REQUIRED)
pybind11_add_module(raytracer 
                    pybindRaytracer.cc 
                    renderer.cpp 
                    shapes/sphere.cpp
                    shapes/plane.cpp
                    shapes/cube.cpp
                    shapes/rectangle.cpp
                    vector.cpp 
                    camera.cpp 
                    ray.cpp
                    materials/diffuse.cpp
                    materials/material.cpp
                    materials/emissive.cpp
                    materials/glass.cpp
                    materials/metal.cpp
                    )

include_directories(${pybind11_INCLUDE_DIRS})