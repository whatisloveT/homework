class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.surname} {self.name}'
        return full_name

    def get_total_income(self):
        total_income = self._income['wage'] * (1 + self._income['bonus'] / 100)
        return f'Доход составляет : {total_income} руб.'


a = Position('Владислав', 'Лапин', 'Инженер-технолог', 18590, 30)
print(a.get_full_name())
print(a.get_total_income())
print(a._income)