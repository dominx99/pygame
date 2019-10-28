class BulletIterator:
   def __init__(self, bullets):
       self.bullets = bullets
       self.index = 0

   def __next__(self):
       if self.index < len(self.bullets.bullets):
            result = (self.bullets.bullets[self.index])
            self.index +=1

            return result

       raise StopIteration
