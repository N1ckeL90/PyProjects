class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехал(-а)')

    def stop(self):
        print(f'{self.color} {self.name} остановился(-ась)')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернул(-а) на {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.color} {self.name} превысил скорость больше 60 км/ч')
        else:
            print(f'Скорость {self.name} - {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.color} {self.name} превысил скорость больше 40 км/ч')
        else:
            print(f'Скорость {self.name} - {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car1 = TownCar(50, 'Белый', 'Chevrolet Cruze')
town_car1.go()
town_car1.stop()
town_car1.show_speed()
print(town_car1.is_police)

town_car2 = TownCar(65, 'Черный', 'Chevrolet Cruze')
town_car2.go()
town_car2.stop()
town_car2.show_speed()
print(town_car2.is_police)

sport_car = SportCar(50, 'Синий', 'Ford GT')
sport_car.go()
sport_car.stop()
sport_car.show_speed()
print(sport_car.is_police)

work_car = WorkCar(50, 'Серый', 'Mersedes Vito')
work_car.go()
work_car.stop()
work_car.show_speed()
print(work_car.is_police)

work_car = WorkCar(30, 'Серый', 'Mersedes Vito')
work_car.go()
work_car.stop()
work_car.show_speed()
print(work_car.is_police)

police_car = PoliceCar(50, 'Синяя', 'Лада Гранта')
police_car.go()
police_car.stop()
police_car.show_speed()
print(police_car.is_police)
