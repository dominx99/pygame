class PointsCollector(object):
    def __init__(self, points, enemies):
        for enemy in enemies:
            enemy.add_listener('pointed', points.increment)
