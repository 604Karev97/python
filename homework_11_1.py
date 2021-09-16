import time
from datetime import date


class Date:
    def __init__(self, date_str):
        self.date_str = time.strptime(date_str, '%d-%m-%Y')

    def __str__(self):
        return time.strftime('%d-%m-%Y', self.date_str)

    @classmethod
    def convert_date(cls, date_str):
        return tuple([int(date_str.split('-')[i]) for i in range(len(date_str.split('-')))])

    @staticmethod
    def validator(date_str):
        lst = Date.convert_date(date_str)
        try:
            date(lst[2], lst[1], lst[0])
            return True
        except ValueError:
            return False


d = Date('16-09-2021')
print(d)
print(d.convert_date(d.__str__()))
print(d.validator(d.__str__()))


