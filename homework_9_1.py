import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    @staticmethod
    def running():
        for color in TrafficLight.__color:
            if color == 'красный':
                print(f'Стоп! Горит {color} свет.')
                time.sleep(7)
            elif color == 'желтый':
                print(f'Приготовиться! Горит {color} свет.')
                time.sleep(2)
            elif color == 'зеленый':
                print(f'Вперед! Горит {color} свет.')
                time.sleep(10)
            else:
                raise ValueError


while True:
    try:
        TrafficLight.running()
    except ValueError:
        print('Нарушен порядок цвета.')
        break
