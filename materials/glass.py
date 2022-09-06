from materials.material import *

class Glass(Material):
    def __init__(self, color=Color(1, 1, 1), idx_refraction=1.5):
        super().__init__(color)
        self.idx_refraction = idx_refraction

    def bounce(self, r, normal, hit_pos):
        outside = r.direction.dot(normal) < 0
        refraction_ratio = self.idx_refraction if not outside else 1 / self.idx_refraction

        normal = normal if outside else -1 * normal

        unit_direction = r.direction.normalize()
        cos_theta = min(-unit_direction.dot(normal), 1)
        sin_theta = sqrt(1 - cos_theta**2)

        cannot_refract = refraction_ratio * sin_theta > 1
        if cannot_refract or Glass.reflectance(cos_theta, refraction_ratio) > random():
            new_direction = Glass.reflect(unit_direction, normal)
        else:
            new_direction = Glass.refract(
                r.direction, normal, refraction_ratio)
        return Ray(hit_pos, new_direction)

    @staticmethod
    def refract(direction, normal, refraction_ratio):
        cos_theta = min((-1 * direction).dot(normal), 1)
        perp = refraction_ratio * (direction + cos_theta * normal)
        parallel = -sqrt(abs(1 - perp.length()**2)) * normal

        return parallel + perp

    @staticmethod
    def reflect(direction, normal):
        return direction - 2 * direction.dot(normal) * normal

    @staticmethod
    def reflectance(cos, reflectance_ratio):
        r0 = (1 - reflectance_ratio) / (1 + reflectance_ratio)
        r0 = r0**2
        return r0 + (1 - r0) * pow((1 - cos), 5)