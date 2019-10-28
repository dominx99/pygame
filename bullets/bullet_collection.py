from settings import Settings

class BulletCollection(object):
    def __init__(self):
        self.bullets = []
        self.size = Settings.SCREEN.get_size()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

    def tick(self):
        self.remove_bullet_on_borders()

        for bullet in self.bullets:
            bullet.tick()

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def anyone_collision_with_enemy(self, enemy):
        collision = False

        for bullet in self.bullets:
            if bullet.collision_with_enemy(enemy):
                collision = True

        return collision

    def remove_bullet_on_borders(self):
        for bullet in self.bullets:
            if bullet.x < 0 or \
               bullet.y > self.size[0] or \
               bullet.y < 0 or \
               bullet.y > self.size[1]:
                self.bullets.remove(bullet)
