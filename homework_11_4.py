class NotNumIntError(Exception):
    pass


class NotNumRealError(Exception):
    pass


class OfficeWare:
    dct_equipments = {}

    @staticmethod
    def validator_int(num):
        try:
            if not type(num) == int:
                raise NotNumIntError()
            else:
                return num
        except NotNumIntError:
            print('Подерживаются данные только целочисленного типа')

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = self.validator_int(capacity)

    def receipt_equipment(self, equip, quantity):
        equip_name = f'{equip.brand} {equip.model} {equip.color}'
        quantity = self.validator_int(quantity)
        if equip_name not in self.dct_equipments:
            self.dct_equipments[equip_name] = quantity
        else:
            self.dct_equipments[equip_name] += quantity
        return f'Склад {self.name} принял {equip_name} в количестве {quantity} шт.'

    def send_equipment(self, equip, quantity, division):
        equip_name = f'{equip.brand} {equip.model} {equip.color}'
        quantity = self.validator_int(quantity)
        if equip_name not in self.dct_equipments:
            print('Данного вида товара на складе нет.')
        elif self.dct_equipments[equip_name] < quantity:
            print('Данного количетсва товара на складе нет.')
        else:
            self.dct_equipments[equip_name] -= quantity
            return f'Склад {self.name} перевел {equip_name} в количестве {quantity} шт в подразделение {division}'

    def print_equipment(self):
        print(self.dct_equipments)


class Equipment:

    @staticmethod
    def validator_real(num):
        try:
            if not type(num) == int and type(num) == float:
                raise NotNumRealError()
            else:
                return num
        except NotNumRealError:
            print('Подерживаются данные только численного типа')

    def __init__(self, brand, model, price, color):
        self.brand = brand
        self.model = model
        self.price = self.validator_real(price)
        self.color = color

    def __str__(self):
        return f'{self.brand} {self.model} {self.color}'


class Printer(Equipment):
    def __init__(self, brand, model, price, color, speed_print, max_papers):
        super().__init__(brand, model, price, color)
        self.speed_print = self.validator_real(speed_print)
        self.max_papers = self.validator_real(max_papers)


class Scanner(Equipment):
    def __init__(self, brand, model, price, color, speed_scan, lvl_scan):
        super().__init__(brand, model, price, color)
        self.speed_scan = self.validator_real(speed_scan)
        self.lvl_scan = self.validator_real(lvl_scan)


class Xerox(Equipment):
    def __init__(self, brand, model, price, color, is_mfu=True):
        super().__init__(brand, model, price, color)
        self.is_mfu = is_mfu


komus = OfficeWare('Komus', 1000)
mvideo = OfficeWare('M-Video', 3000)

hp_p = Printer('HP', 'MP-205', 15000, 'black', 30, 250)
samsung_p = Printer('Samsung', '890-321', 20000, 'white', 25, 300)
epson_p = Printer('Epson', 'XFR', 10000, 'gray', 20, 400)
hp_s = Scanner('HP', 'MP-500', 10000, 'black', 10, 250)
samsung_s = Scanner('Samsung', '900-321', 15000, 'white', 10, 125)
epson_s = Scanner('Epson', 'XFXXX', 5000, 'gray', 20, 125)
hp_x = Xerox('HP', 'X-500', 5000, 'black')
samsung_x = Xerox('Samsung', '1000', 10000, 'white')
epson_x = Xerox('Epson', 'Xerox', 5000, 'gray', is_mfu=False)

print(komus.receipt_equipment(hp_p, 100))
print(komus.receipt_equipment(hp_x, 300))
print(komus.receipt_equipment(hp_p, 10))
print(komus.receipt_equipment(hp_s, 50))
print(komus.receipt_equipment(hp_p, 50))
print(komus.dct_equipments)

print(komus.send_equipment(hp_p, 30, 'ООО Ромашка'))
print(komus.dct_equipments)

print(komus.send_equipment(hp_p, 1000, 'ООО Ромашка'))
print(komus.dct_equipments)

komus.print_equipment()
