from vector import Vector
from ray import Ray
from main import clamp

v = Vector(1, 1, 1)
# print(v.length())

# print(v.dot(v))

print(clamp(1.000001, 0, 1))
print(clamp(34.2, 0, 34))
print(clamp(45, 0, 10))
print(clamp(1, 0, 1))
print(clamp(-101, 0, 100))