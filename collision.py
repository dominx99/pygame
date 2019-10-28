class Collision(object):
    def __init__(self, x, y):
        if isinstance(x, object) and isinstance(y, object):
            self.collection_collisions(x, y)
            return

        self.object_collisions(x, y)

    def object_collisions(self, x, y):
        if x.collision(y):
            x.emit_event('collision', y)

    def collection_collisions(self, collectionX, collectionY):
        for x in collectionX:
            for y in collectionY:
                if x.hasCollision(y):
                    x.emit_event('collision', y)
