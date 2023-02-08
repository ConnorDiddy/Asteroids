import math
from movable import Movable

class Rotatable(Movable):
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, world_width, world_height)
        self.mX = x
        self.mY = y
        self.mDX = dx
        self.mDY = dy
        self.mRotation = rotation
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height

    def rotate(self, delta_rotation):
        self.mRotation += delta_rotation
        if self.mRotation >=360:
            self.mRotation -= 360
        if self.mRotation < 0:
            self.mRotation += 360

    def splitDeltaVIntoXAndY(self, rotation, delta_velocity):
        rotation_radians = math.radians(rotation)
        x_velocity = delta_velocity * math.cos(rotation_radians)
        y_velocity = delta_velocity * math.sin(rotation_radians)
        return (x_velocity, y_velocity)

    def accelerate(self, delta_velocity):
        x_velocity, y_velocity = self.splitDeltaVIntoXAndY(self.mRotation, delta_velocity)
        self.mDX += x_velocity
        self.mDY += y_velocity

    def decelerate(self, delta_velocity):
        if 0 < self.mDX < delta_velocity:
            self.mDX = 0
        if 0 < self.mDY < delta_velocity:
            self.mDY = 0

        if self.mDX > 0:
            self.mDX -= delta_velocity
        if self.mDX < 0:
            self.mDX += delta_velocity
        if self.mDY > 0:
            self.mDY -= delta_velocity
        if self.mDY < 0:
            self.mDY += delta_velocity
        

    def rotatePoint(self, x, y):
        rotation_radians = math.radians(self.mRotation)
        new_x = x * math.cos(rotation_radians) - y * math.sin(rotation_radians)
        new_y = x * math.sin(rotation_radians) + y * math.cos(rotation_radians)
        return (new_x, new_y)

    def translatePoint(self, x, y):
        new_x = x + self.mX
        new_y = y + self.mY
        return (new_x, new_y)

    def rotateAndTranslatePoint(self, x, y):
        rotated_point = self.rotatePoint(x, y)
        translated_point = self.translatePoint(*rotated_point)
        return translated_point

    def rotateAndTranslatePointList(self, point_list):
        translated_list = []
        for point in point_list:
            translated_point = self.rotateAndTranslatePoint(*point)
            translated_list.append(translated_point)
        return translated_list

    def getRotation(self):
        return self.mRotation
