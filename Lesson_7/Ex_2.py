from abc import ABC, abstractmethod


class Clothes:
    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    def cloth_consumption(self):
        return self.v / 6.5 + 0.5

    @property
    def size(self):
        return self.v


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    def cloth_consumption(self):
        return 2 * self.h + 0.3

    @property
    def height(self):
        return self.h


a = Coat(46)
b = Suit(2)
print(a.cloth_consumption())
print(b.cloth_consumption())
print(a.size)
print(b.height)
