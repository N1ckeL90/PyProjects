# Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведённых типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
class Warehouse:
    def __init__(self, unit, number):
        self.unit = unit
        self.number = number


class OfficeEquipment:
    def __init__(self, type_equip):
        self.type_equip = type_equip


class Printer(OfficeEquipment):
    def __init__(self, brand, model):
        type_equip = 'Printer'
        super().__init__(type_equip)
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'{self.type_equip} {self.brand} {self.model}'


class Scanner(OfficeEquipment):
    def __init__(self, brand, model):
        type_equip = 'Scanner'
        super().__init__(type_equip)
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'{self.type_equip} {self.brand} {self.model}'


class Xerox(OfficeEquipment):
    def __init__(self, brand, model):
        type_equip = 'Xerox'
        super().__init__(type_equip)
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'{self.type_equip} {self.brand} {self.model}'


printer1 = Printer('HP', 'Ink Tank 410')
print(printer1)
scanner1 = Scanner('Canon', 'imageFORMULA DR-F120')
print(scanner1)
xerox1 = Xerox('Xerox', 'WorkCentre 3025BI')
print(xerox1)

