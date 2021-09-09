class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась.')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}.')

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Машина {self.name} превысила скорость на {self.speed - 60} км/ч.') if self.speed > 60 else print(
            f'Текущая скорость {self.name}: {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Машина {self.name} превысила скорость на {self.speed - 40} км/ч.') if self.speed > 40 else print(
            f'Текущая скорость {self.name}: {self.speed} км/ч')


class PoliceCar(Car):
    pass


thunder = SportCar(160, 'red', 'Thunder')
rumbo = WorkCar(40, 'white', 'Rumbo')
pony = WorkCar(30, 'gray', 'Pony')
admiral = TownCar(60, 'black', 'Admiral')
stallion = TownCar(55, 'blue', 'Stallion')
vcpd = PoliceCar(90, 'black-white', 'Police', True)

lst = [thunder, rumbo, pony, admiral, stallion, vcpd]

for car in lst:
    if car.speed <= 40:
        car.speed = 50
    car.show_speed()

print('-' * 40)

for car in lst:
    if car.speed <= 60:
        car.speed = 70
    car.show_speed()
