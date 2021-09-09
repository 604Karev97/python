class Road:
    def __init__(self, lngth, wdth):
        self._length = lngth
        self._width = wdth

    def calc_mass(self, thick, weight):
        mass = self._width * self._length * weight * thick
        return mass


print('Нужно ввести параметры дороги:')
road = Road(float(input(' - введите длину (м): ')),
            float(input(' - введите ширину (м): ')))
mass_road = road.calc_mass(float(input(' - введите толщину покрытия (м): ')),
                           float(input(' - введите массу 1 кв.м покрытия (кг): ')))
print(f'Масса асфальта составляет: {mass_road / 1000} т.')
