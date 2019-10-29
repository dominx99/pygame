import pygame, random
from settings import Settings
from pyjon.events import EventDispatcher

class Enemy(object, metaclass = EventDispatcher):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 3
        self.width = 20
        self.height = 20
        self.points = 3

    def draw(self):
        rect = pygame.draw.rect(Settings.SCREEN, (255, 0, 0), pygame.Rect(self.x, self.y, 20, 20))

    def get_shot(self, bullet):
        self.reduce_health(bullet.power)

        bullet.emit_event('remove')

        if (self.health < 1):
            self.emit_event('remove', self)
            self.emit_event('pointed', 3)

    def reduce_health(self, power):
        self.health -= power
