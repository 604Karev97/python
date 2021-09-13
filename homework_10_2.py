from abc import ABC


class Clothes(ABC):
    def __init__(self):
        self._cloth = 0

    def __str__(self):
        return f"{self.__class__.__name__} ({self.cloth:.2f})"

    @property
    def cloth(self):
        if not self._cloth:
            self._cloth = self.calc_cloth()
        return self._cloth

    def calc_cloth(self):
        raise NotImplementedError(self.__class__.__name__)

    def __add__(self, other):
        result = Clothes()
        result._cloth = self.cloth + other.cloth
        return result

    def __radd__(self, other):
        if not isinstance(other, Clothes):
            return self
        return self.__add__(other)


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self._size = float(size)

    def calc_cloth(self):
        return self._size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, tall):
        super().__init__()
        self._tall = float(tall)

    def calc_cloth(self):
        return 2 * self._tall + 0.3


if __name__ == '__main__':
    coat_1 = Coat(48)
    suit_1 = Suit(100)
    coat_2 = Coat(20)
    suit_2 = Suit(50)
    print(coat_1)
    print(suit_1)
    print(coat_2)
    print(suit_2)
    print(coat_1 + suit_1 + coat_2 + suit_2)
    print(sum([coat_1, suit_1, coat_2, suit_2]))
