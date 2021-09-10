class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police

    def go(self):
        print(f'Автомобиль {self.name} тронулся')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} поворачивает на {direction}')

    def show_speed(self):
        if type(self.speed) == int:
            print(f'Текущая скорость автомобиля {self.name} : {self.speed}')
        else:
            raise ValueError(f'Введите корректную скорость в километрах')


class TownCar(Car):
    def show_speed(self):
        if type(self.speed) == int:
            if self.speed > 60:
                print(f'ВНИМАНИЕ! Нарушен скоростно режим. Максимально допустима скорость равна 60')
            else:
                print(f'Текущая скорость автомобиля : {self.speed}')
        else:
            raise ValueError(f'Введите корректную скорость в километрах')


class SportCar(Car):
    pass

class WorkCar(Car):
    def __init__(self, speed, color, name, is_trailer):
        super().__init__(speed, color, name)
        self.trailer = is_trailer
        pass

    def in_trailer(self):
        if self.trailer:
            input('Что погрузим в прицеп ?')
        else:
            print('Едем на легке!')

    def show_speed(self):
        if type(self.speed) == int:
            if self.speed > 40:
                print(f'ВНИМАНИЕ! Нарушен скоростно режим. Максимально допустима скорость равна 40')
            else:
                print(f'Текущая скорость автомобиля : {self.speed}')
        else:
            raise ValueError(f'Введите корректную скорость в километрах')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
        pass
    def check_police(self):
        print(f'Автомобиль {self.name} полицески {self.is_polise}')


a = TownCar(61, 'Red', 'Mazda')
b = TownCar('dfdf', 'Black', 'Lada')
c = SportCar(125, 'Black', 'Lexus')
d = WorkCar(39,'Blue', 'Chevrrolet', True )
e = PoliceCar(125, 'Black', 'Lexus')
a.go()
a.turn('лево')
a.stop()
a.show_speed()
b.show_speed()
d.show_speed()
d.in_trailer()