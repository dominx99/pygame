class EnemyIterator:
   def __init__(self, enemies):
       self.enemies = enemies
       self.index = 0

   def __next__(self):
       if self.index < len(self.enemies.enemies):
            result = (self.enemies.enemies[self.index])
            self.index +=1
            return result

       raise StopIteration
