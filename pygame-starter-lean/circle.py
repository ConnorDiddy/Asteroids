from rotatable import Rotatable
import pygame

class Circle(Rotatable):
    def __init__(self, x, y, dx, dy, rotation, radius, world_width, world_height):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self.mRadius = radius
        self.mColor = (255, 255, 255)

    def setRadius(self, radius):
        if radius >= 1:
            self.mRadius = radius

    def getColor(self):
        return self.mColor

    def getRadius(self):
        return self.mRadius
        
    def setColor(self, color):
        self.mColor = color
        
    def draw(self, surface):
        tuple = (self.getX(), self.getY())
        pygame.draw.circle(surface, self.mColor, tuple, self.mRadius)


