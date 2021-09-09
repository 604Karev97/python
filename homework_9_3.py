class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self._income = {}
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    @staticmethod
    def get_full_name(worker):
        return f'{worker.name} {worker.surname}'

    @staticmethod
    def get_total_income(worker):
        return (worker._income['wage'] + worker._income['bonus'])


ivan = Worker('Ivan', 'Petrov', 'dev', 50000, 0)
eliza = Worker('Eliza', 'Bondareva', 'sec', 45000, 1000)
ksenia = Worker('Ksenya', 'Lebedeva', 'man', 65000, 5000)

lst = [ivan, eliza, ksenia]

[print(f'ФИО: {Position.get_full_name(i)}, ЗП: {Position.get_total_income(i)}') for i in lst]
