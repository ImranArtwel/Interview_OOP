from abc import abstractmethod,ABCMeta
from math import sqrt
class Animal(object):
    __metaclass__ = ABCMeta
    

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def moveUp(self,y_val):

        self.y = self.y + y_val

    def moveDown(self,y_val):

        self.y = self.y + y_val
  
    def moveRight(self,x_val):

        self.x = self.x + x_val

    def moveLeft(self,x_val):

        self.x = self.x + x_val

   
    def distance(self, object):
        print(object)
        dist = sqrt( (object.x - self.x)**2 + (object.y - self.y)**2 )
        return dist
            

    
         


