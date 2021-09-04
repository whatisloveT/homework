from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def total_consum(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def total_consum(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def total_consum(self):
        return self.height * 2 + 0.3


a = Coat(58)
print(a.total_consum)
b = Costume(190)
print(b.total_consum)
