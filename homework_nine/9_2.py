import random


class Road:
    mass_of_asph = [25.7, 24.6, 24.9, 25.0, 23.2, 24.8, 24.2, 25.8,
                    25.7]  # масса асфальта необходимого на 1 кв. м толщиной 1 см в зависимости от типа смеси

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self):
        temp_mass = random.choice(Road.mass_of_asph)
        temp_thickness = random.randint(1, 10)    # Случаная толщина покрытия от 1 до 10 см
        request_mass = (self._length * self._width * temp_mass * temp_thickness) / 1000
        print(f'Для покрытия потребуется : {request_mass} т. асфальта')


a = Road(15, 3524)
a.mass_calc()