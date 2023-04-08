cmake_minimum_required(VERSION 3.11.0)
project(raytracer VERSION 0.1.0)

# For Apple, use the following to compile:
# cmake -D CMAKE_CXX_COMPILER=g++-12 ..

# Set OpenMP root directory on macOS
if (APPLE)
    execute_process(
        COMMAND brew --prefix libomp
        OUTPUT_VARIABLE LIBOMP_PREFIX
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    set(OpenMP_ROOT ${LIBOMP_PREFIX})
endif()

cmake_policy(SET CMP0074 NEW)

# Set C standard to C11
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Set C++ standard to C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_subdirectory(extern/pybind11)
find_package(OpenMP)

pybind11_add_module(raytracer 
                    pybindRaytracer.cc 
                    renderer.cpp 
                    shapes/sphere.cpp
                    shapes/plane.cpp
                    shapes/cube.cpp
                    shapes/rectangle.cpp
                    shapes/disc.cpp
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

if(OpenMP_CXX_FOUND)
    target_link_libraries(raytracer PUBLIC OpenMP::OpenMP_CXX)
    target_compile_definitions(raytracer PUBLIC USE_OPENMP)
    message(STATUS "Using OpenMP")
endif()
