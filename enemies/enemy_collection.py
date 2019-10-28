import random
from settings import Settings
from enemies.enemy import Enemy

class EnemyCollection(object):
    def __init__(self):
        self.enemies = []
        self.size = Settings.SCREEN.get_size()

    def draw(self):
        for enemy in self.enemies:
            enemy.draw()

    def tick(self):
        self.spawn_randomly()

    def spawn_randomly(self):
        if len(self.enemies) < 7:
            self.enemies.append(Enemy(random.randint(10, self.size[0] - 10), random.randint(1, self.size[1] - 10)))

    def destroy_on_collision(self, bullets):
        for enemy in self.enemies:
            if bullets.anyone_collision_with_enemy(enemy):
                self.enemies.remove(enemy)
