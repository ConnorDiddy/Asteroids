import math
import pygame
from rotatable import Rotatable

class Polygon(Rotatable):
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self.mOriginalPolygon = []
        self.mColor = (255,255,255)
        #self.mPoints = points

    def setPolygon(self, polygon):
        self.mOriginalPolygon = polygon

    def setColor(self, color):
        self.mColor = color

    def draw(self, screen):
        rotated_and_translated_polygon = [self.rotateAndTranslatePoint(*point) for point in self.mOriginalPolygon]
        pygame.draw.polygon(screen, self.mColor, rotated_and_translated_polygon)

    def getPolygon(self):
        return self.mOriginalPolygon

    def getColor(self):
        return self.mColor

    def getRadius(self):
        total_distance = 0
        for point in self.mOriginalPolygon:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            total_distance += distance
        if len(self.mOriginalPolygon) > 0:
            return total_distance / len(self.mOriginalPolygon)
        else:
            return 0
