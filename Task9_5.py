class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')


pen = Pen('Brauberg')
pen.draw()
pencil = Pencil('Bic')
pencil.draw()
handle = Handle('Deli')
handle.draw()
