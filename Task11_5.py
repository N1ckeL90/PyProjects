class Warehouse:
    position = 1

    def __init__(self, database):
        self.database = database

    def take_device(self):
        type_device = input('Введите тип устройства (принтер, сканер или ксерокс): ')
        brand = input('Введите марку производителя: ')
        model = input('Введите название модели: ')
        number = int(input('Введите количество устройств: '))
        self.database[Warehouse.position] = [type_device, brand, model, number]
        Warehouse.position += 1

    def transfer_device(self):
        company_division = input('Введите название комании для передачи:')
        brand = input('Введите марку производителя: ')
        model = input('Введите название модели: ')
        number = int(input('Введите количество устройств: '))
        delete_command = False
        delete_key = 0
        device_found = False
        for key_, value_ in self.database.items():
            if value_[1].lower() == brand.lower() and value_[2].lower() == model.lower():
                device_found = True
                dif = (value_[3] - number)
                if dif >= 0:
                    self.database[key_] = [value_[0], value_[1], value_[2], dif]
                    if dif == 0:
                        delete_command = True
                        delete_key = key_
                    print(f'{value_[0]} {value_[1]} {value_[2]} - {number} шт. передано комании {company_division}')
                elif dif < 0:
                    print('Неверный ввод числа передаваемых устройств')
        if delete_command:
            del self.database[delete_key]
        if not device_found:
            print('Устройство не найдено. Проверьте правильность ввода даных')


class OfficeEquipment:
    def __init__(self, type_device):
        self.type_device = type_device


class Printer(OfficeEquipment):
    def __init__(self, brand, model):
        type_device = 'Printer'
        super().__init__(type_device)
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'{self.type_device} {self.brand} {self.model}'


class Scanner(OfficeEquipment):
    def __init__(self, brand, model):
        type_device = 'Scanner'
        super().__init__(type_device)
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'{self.type_device} {self.brand} {self.model}'


class Xerox(OfficeEquipment):
    def __init__(self, brand, model):
        type_device = 'Xerox'
        super().__init__(type_device)
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'{self.type_device} {self.brand} {self.model}'


data = {}
transfer_list = {}
sklad = Warehouse(data)
while True:
    command = input("Для добавления оргтехники на склад, введите '1';\n"
                    "Для передачи оргтехники в другое подразделение, введите '2';\n"
                    "Для просмотра огтехники на складе, введите '3'\n"
                    "для выхода нажмите 'q':\n")
    if command == 'q':
        break
    elif command == '1':
        sklad.take_device()
    elif command == '2':
        sklad.transfer_device()
    elif command == '3':
        for value in data.values():
            print(f'{value[0]} {value[1]} {value[2]} - {value[3]} шт. ')
