import math


class Cylinder:
    def __init__(self, height, radius):
        self.set_height(height)
        self.set_radius(radius)

    def get_height(self):
        return self.height

    def set_height(self, height):
        if 0 <= height <= 10:
            self.height = height
        else:
            raise ValueError("A altura do cilindro deve estar entre 0 e 10.")

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if 0 <= radius <= 10:
            self.radius = radius
        else:
            raise ValueError("O raio do cilindro deve estar entre 0 e 10.")

    def base_area(self):
        return math.pi * self.radius**2

    def lateral_area(self):
        return 2 * math.pi * self.height * self.radius

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.height + self.radius)

    def volume(self):
        return math.pi * self.height * self.radius**2


# main

height, radius = map(int, input().split())
cylinder = Cylinder(height, radius)

print("Altura do cilindro:", cylinder.get_height())
print("Raio do cilindro:", cylinder.get_radius())
print("Área da base:", cylinder.base_area())
print("Área lateral:", cylinder.lateral_area())
print("Área total:", cylinder.surface_area())
print("Volume:", cylinder.volume())
