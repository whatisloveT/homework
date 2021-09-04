class Cell:
    def __init__(self, quantity=int):
        if type(quantity) != int:
            raise ValueError('Необходимо ввести целое число клеток')
        else:
            self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        return self.quantity - other.quantity if self.quantity > other.quantity else 'Вычитание невозможно'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __floordiv__(self, other):
        return self.quantity // other.quantity

    def __truediv__(self, other):
        return self.quantity / other.quantity

    def make_order(self, number):
        int_dir = self.quantity // number
        ream_dir = self.quantity % number
        if int_dir > 1 :
            print(('*'*number+'\n') * int_dir + '*'*ream_dir+'\n')
        else:
            print('*' * ream_dir + '\n')


a = Cell(21)
b = Cell(19)
print(a-b)
print(a+b)
print(a/b)
a.make_order(7)
