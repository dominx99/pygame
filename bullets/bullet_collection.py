from settings import Settings
from pyjon.events import EventDispatcher
from bullets.bullet_iterator import BulletIterator

class BulletCollection(object, metaclass = EventDispatcher):
    def __init__(self):
        self.bullets = []
        self.size = Settings.SCREEN.get_size()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

    def tick(self):
        self.remove_bullet_on_borders()
        self.remove_destroyed_bullets()

        for bullet in self.bullets:
            bullet.tick()

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def remove(self, bullet):
        self.bullets.remove(bullet)

    def remove_bullet_on_borders(self):
        for bullet in self.bullets:
            if bullet.x < 0 or \
               bullet.y > self.size[0] or \
               bullet.y < 0 or \
               bullet.y > self.size[1]:
                self.bullets.remove(bullet)

    def remove_destroyed_bullets(self):
        for bullet in self.bullets:
            if bullet.destroyed:
                self.bullets.remove(bullet)

    def __iter__(self):
        return BulletIterator(self)
