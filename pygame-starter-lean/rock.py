import random
import math
from polygon import Polygon

class Rock(Polygon):
    def __init__(self, x, y, world_width, world_height):
        rotation = random.uniform(0, 359.9)
        spin_rate = random.uniform(-90, 90)
        acceleration = random.uniform(10, 20)
        radius = random.uniform(20, 40)
        number_of_points = random.randint(5, 12)
        super().__init__(x, y, 0, 0, rotation, world_width, world_height)
        self.mSpinRate = spin_rate
        self.setPolygon(self.createRandomPolygon(radius, number_of_points))
        self.accelerate(acceleration)

    def createRandomPolygon(self, radius, number_of_points):
        point_list = []
        angle_increment = 360 / number_of_points
        for i in range(number_of_points):
            angle = i * angle_increment
            distance = radius * random.uniform(0.7, 1.3)
            x = distance * math.cos(math.radians(angle))
            y = distance * math.sin(math.radians(angle))
            point_list.append((x, y))
        return point_list

    def evolve(self, dt):
        self.move(dt)
        self.mRotation += self.mSpinRate * dt

    def setSpinRate(self, spin_rate):
        self.mSpinRate = spin_rate

    def getSpinRate(self):
        return self.mSpinRate
