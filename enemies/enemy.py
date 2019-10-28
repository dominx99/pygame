import pygame, random
from settings import Settings

class Enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(Settings.SCREEN, (255, 0, 0), pygame.Rect(self.x, self.y, 20, 20))
