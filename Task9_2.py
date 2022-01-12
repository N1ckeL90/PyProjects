class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, depth, mass):

        return f'{self._length} м * {self._width} м * {depth} см * {mass} кг = ' \
                      f'{int((self._length * self._width * depth * mass) / 1000)} т. '


tmp = Road(20, 50000)
print(tmp.calc_mass(5, 25))
