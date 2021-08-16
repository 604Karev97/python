error_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
              'директор аэлита']
name_list = []

[name_list.append(data.split(' ')[-1]) for data in error_list]

[print(f'Привет, {name.lower().title()}!') for name in name_list]
