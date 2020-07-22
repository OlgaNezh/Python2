from abc import ABC, abstractmethod

class Clothes (ABC):
    name = None

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def fabric_use(self):
        pass

class Coat(Clothes):
    name = 'пальто'
    def __init__(self, v):
        self.v = v

    def __str__(self):
        return '[' + self.name + ' размер ' + str(self.v) + ']'

    @property
    def fabric_use(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    name = 'клстюм'

    def __init__(self, h):
        self.h = h

    def __str__(self):
        return '[' + self.name + ' размер ' + str(self.h) + ']'

    @property
    def fabric_use(self):
        return 2 * self.h + 0.3

coat = Coat(42)

print(coat, 'требуется ткани: ', coat.fabric_use)

suit = Suit(165)
print(suit, 'требуется ткани: ', suit.fabric_use)
