from qstn_2 import Animal

class Dog(Animal):
        def __init__(self,x,y):
            super(Dog,self).__init__(x,y)

        def currP(self):
            return '{} {}'.format(self.x,self.y)
            

                           

