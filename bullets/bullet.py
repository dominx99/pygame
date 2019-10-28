import pygame
from pygame.math import Vector2
from settings import Settings

class Bullet(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.radius = 2
        self.draw()
        self.tick()

    def tick(self):
        self.x += -self.direction.y * 2
        self.y += self.direction.x * 2

    def draw(self):
        pygame.draw.circle(Settings.SCREEN, (255,0,0), (int(self.x), int(self.y)), 3)

    def collision_with_enemy(self, enemy):
        if self.x - self.radius < enemy.x + 20 and \
           self.x + self.radius > enemy.x and \
           self.y + self.radius > enemy.y and \
           self.y - self.radius < enemy.y + 20:
            return True

        return False
