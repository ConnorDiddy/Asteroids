import random
from ship import Ship
from rock import Rock
from star import Star

class Asteroids:
    def __init__(self, width, height):
        self.mWorldWidth = width
        self.mWorldHeight = height
        self.mShip = Ship(width/2, height/2, width, height)
        self.mRocks = [Rock(random.uniform(0, width), random.uniform(0, height), width, height) for i in range(10)]
        self.mBullets = []
        self.mStars = [Star(random.uniform(0, width), random.uniform(0, height), width, height) for i in range(20)]
        self.mObjects = [self.mShip] + self.mRocks + self.mBullets + self.mStars

    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def getShip(self):
        return self.mShip

    def getRocks(self):
        return self.mRocks

    def getObjects(self):
        return self.mObjects

    def getBullets(self):
        return self.mBullets

    def getStars(self):
        return self.mStars

    def evolveAllObjects(self, dt):
        for obj in self.mObjects:
            obj.evolve(dt)

    def turnShipLeft(self, delta_rotation):
        self.mShip.rotate(delta_rotation * -1)

    def turnShipRight(self, delta_rotation):
        self.mShip.rotate(delta_rotation)

    def accelerateShip(self, delta_velocity):
        self.mShip.accelerate(delta_velocity)

    def decelerateShip(self, delta_velocity):
        self.mShip.decelerate(delta_velocity)

    def fire(self):
        if len(self.mBullets) < 3:
            bullet = self.mShip.fire()
            self.mBullets.append(bullet)
            self.mObjects.append(bullet)
            return bullet
        return None

    def draw(self, surface, objects):
        surface.fill((0,0,0))
        for obj in objects:
            if obj.mActive:
                obj.draw(surface)

    def removeInactiveObjects(self):
        self.mObjects = [obj for obj in self.mObjects if obj.getActive()]
        self.mRocks = [rock for rock in self.mRocks if rock.getActive()]
        self.mBullets = [bullet for bullet in self.mBullets if bullet.getActive()]
        self.mStars = [star for star in self.mStars if star.getActive()]

    def collideShipAndBullets(self):
        for bullet in self.mBullets:
            if self.mShip.hits(bullet):
                self.mShip.setActive(False)
                bullet.setActive(False)

    def collideShipAndRocks(self):
        for rock in self.mRocks:
            if self.mShip.hits(rock):
                self.mShip.setActive(False)
                rock.setActive(False)

    def collideRocksAndBullets(self, debug=False):
        for rock in self.mRocks:
            for bullet in self.mBullets:
                if rock.hits(bullet):
                    rock.setActive(False)
                    bullet.setActive(False)
        return

    def evolve(self, dt, time_passed):
        for obj in self.mObjects:
            obj.evolve(dt)

        if time_passed > 3:
            self.collideShipAndBullets()
            self.collideShipAndRocks()
            self.collideRocksAndBullets()
            self.removeInactiveObjects()