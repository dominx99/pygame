import pygame
from settings import Settings

class PointCollection(object):
    def __init__(self):
        self.amount = 0

    def increment(self, value = 1):
        self.amount = self.amount + value

    def draw(self):
        font = pygame.font.SysFont("Arial", 24)
        text = font.render(str(self.amount), True, (0, 128, 0))

        Settings.SCREEN.blit(text, (
            Settings.RESOLUTION[0] - 15 - text.get_width(),
            15
        ))
