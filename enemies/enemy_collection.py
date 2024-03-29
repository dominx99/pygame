import random
from settings import Settings
from enemies.enemy import Enemy
from enemies.enemy_iterator import EnemyIterator

class EnemyCollection(object):
    def __init__(self, playerPoints):
        self.enemies = []
        self.size = Settings.SCREEN.get_size()
        self.playerPoints = playerPoints

    def draw(self):
        for enemy in self.enemies:
            enemy.draw()

    def tick(self):
        if len(self.enemies) < 15:
            self.spawn_randomly()

    def remove(self, enemy):
        self.enemies.remove(enemy)

    def spawn_randomly(self):
        enemy = Enemy(random.randint(10, self.size[0] - 10), random.randint(1, self.size[1] - 10))
        enemy.add_listener('remove', self.remove)
        enemy.add_listener('pointed', self.playerPoints.increment)

        self.enemies.append(enemy)

    def __iter__(self):
        return EnemyIterator(self)
