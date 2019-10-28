import pygame
from pygame.math import Vector2
from settings import Settings
from pyjon.events import EventDispatcher

class Bullet(object, metaclass = EventDispatcher):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.radius = 2
        self.power = 1
        self.speed = 4
        self.destroyed = False
        self.draw()
        self.tick()

        self.add_listener('collision', self.collision)
        self.add_listener('remove', self.remove)

    def remove(self):
        self.destroyed = True

    def tick(self):
        if (self.destroyed):
            return

        self.x += -self.direction.y * self.speed
        self.y += self.direction.x * self.speed

    def draw(self):
        if (self.destroyed):
            return

        pygame.draw.circle(Settings.SCREEN, (0,0,255), (int(self.x), int(self.y)), 3)

    def hasCollision(self, enemy):
        if self.x - self.radius < enemy.x + enemy.width and \
           self.x + self.radius > enemy.x and \
           self.y + self.radius > enemy.y and \
           self.y - self.radius < enemy.y + enemy.height:
            return True

        return False

    def collision(self, enemy):
        enemy.get_shot(self)
