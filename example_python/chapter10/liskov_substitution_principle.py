#!/usr/bin/python3


class Bird:
    pass

class FlyingBird(Bird):
    def flying(self):
        print('flying')

class Sparrow(FlyingBird):
    pass

def make_it_fly(bird: FlyingBird):
    bird.flying()

#sparrow = Sparrow()
#sparrow.fly()

make_it_fly(Sparrow())


