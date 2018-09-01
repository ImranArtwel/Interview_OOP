from qstn_2 import Animal

class Cat(Animal):
        def __init__(self,x,y):
            super(Cat,self).__init__(x,y)

        def currP(self):
            return '{} {}'.format(self.x,self.y)
            

                           

