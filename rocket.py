import pygame
from pygame.math import Vector2
from bullets.bullet_collection import BulletCollection
from bullets.bullet import Bullet
from settings import Settings
from pyjon.events import EventDispatcher

class Rocket(object):
    def __init__(self):
        self.airResistance = 0.9
        self.speed = 0.1
        self.gravity = 0.0

        self.screen_size = Settings.SCREEN.get_size()

        self.pos = Vector2(self.screen_size[0]/2,self.screen_size[1]/2)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)
        self.angle = Vector2(0,0)
        self.direction = Vector2(1,0)

        self.bullets = BulletCollection()
        # self.points  = PointCollection()
        self.bullets.add_listener('killed', self.add_point)

    def add_point(self):
        # self.points.increment()
        print("point")

    def add_force(self, force):
        self.acc += force

    def border_collision(self):
       if self.pos.x+20 >= self.screen_size[0] or \
          self.pos.x-20 <= 0 or \
          self.pos.y+20 >= self.screen_size[1] or \
          self.pos.y-20 <= 0:
            self.pos = Vector2(self.screen_size[0]/2,self.screen_size[1]/2)

    def physic(self):
        self.vel *= self.airResistance
        self.vel -= Vector2(0, -self.gravity)

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0, -self.speed))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, self.speed))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.speed, 0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.speed, 0))

    def tick(self):
        self.input()
        self.physic()

        self.direction = Vector2(1,0).rotate(-self.angle)

        self.border_collision()
        self.bullets.tick()

    def draw(self):
        points = [Vector2(0, -10), Vector2(5, 5), Vector2(-5, 5)]

        self.angle = self.vel.angle_to(Vector2(0, 1))

        points = [p.rotate(self.angle) for p in points]

        points = [Vector2(p.x, p.y *- 1) for p in points]
        self.points = [Vector2(self.pos+p*2) for p in points]

        pygame.draw.polygon(Settings.SCREEN, (0,100,255), self.points)

        self.bullets.draw()
        # self.points.draw()

    def fire_bullet(self):
        self.bullets.add_bullet(Bullet(
            self.pos.x - (self.direction.y * 17), self.pos.y + (self.direction.x * 17), self.direction
        ))
