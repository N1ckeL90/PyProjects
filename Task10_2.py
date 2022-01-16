from abc import ABC, abstractmethod


class Clothes(ABC):
    consumption_count = 0

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.consumption_count += self.consumption

    def __str__(self):
        return f'Пальто: размер {self.size}, расход ткани {self.consumption}, общий расход ткани {Coat.consumption_count}'

    @property
    def consumption(self):
        exp = self.size / 6.5 + 0.5
        return float(f'{exp:.02f}')


class Costume(Clothes):
    def __init__(self, size):
        self.size = size
        Costume.consumption_count += self.consumption

    def __str__(self):
        return f'Костюм: размер {self.size}, расход ткани {self.consumption}, общий расход ткани ' \
               f'{Costume.consumption_count} '

    @property
    def consumption(self):
        exp = self.size * 2 + 0.3
        return float(f'{exp:.02f}')


coat1 = Coat(50)
print(coat1)
costume1 = Costume(50)
print(costume1)
costume2 = Costume(50)
print(costume2)
