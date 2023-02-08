from polygon import Polygon
from bullet import Bullet

class Ship(Polygon):
    def __init__(self, x, y, world_width, world_height):
        super().__init__(x, y, 0, 0, 0, world_width, world_height)
        self.setPolygon([(10,0), (-10,5), (-5,0), (-10,-5)])

    def evolve(self, dt):
        self.move(dt)

    def fire(self):
        x, y = self.rotateAndTranslatePoint(self.mOriginalPolygon[0][0], self.mOriginalPolygon[0][1])
        bullet = Bullet(x, y, self.getDX(), self.getDY(), self.getRotation(), self.getWorldWidth(), self.getWorldHeight())

        return bullet


