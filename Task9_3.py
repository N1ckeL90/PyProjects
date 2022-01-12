class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        income_dict = {'Wage': wage, 'bonus': bonus}
        self._income = income_dict['Wage'] + income_dict['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income


worker = Position('Ivan', 'Ivanov', 'driver', 40000, 10000)
print(worker.get_full_name())
print(worker.get_total_income())
