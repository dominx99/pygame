import pygame, sys
from rocket import Rocket
from enemies.enemy_collection import EnemyCollection
from settings import Settings

class Game(object):
    def __init__(self):
        pygame.init()

        self.tps_delta = 0.0
        self.tps_clock = pygame.time.Clock()

        self.player = Rocket()
        self.enemies = EnemyCollection()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.player.fire_bullet()

            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / Settings.MAX_TPS:
                self.tick()
                self.tps_delta -= 1 / Settings.MAX_TPS

            Settings.SCREEN.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()
        self.enemies.tick()
        self.enemies.destroy_on_collision(self.player.bullets)

    def draw(self):
        self.player.draw()
        self.enemies.draw()

if __name__ == "__main__":
    Game()
