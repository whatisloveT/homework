class Statyonary:
    title = "Parent"

    def raw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Statyonary):
    def __init__(self):
        self.title = 'Pen'
        pass

    def raw(self):
        print(f'Запуск отрисовки {self.title}')

class Pencil(Statyonary):
    def __init__(self):
        self.title = 'Pencil'
        pass

    def raw(self):
        print(f'Запуск отрисовки {self.title}')

class Handle(Statyonary):
    def __init__(self):
        self.title = 'Handle'
        pass

    def raw(self):
        print(f'Запуск отрисовки {self.title}')

a = Statyonary()
b = Pen()
c = Pencil()
d = Handle()
a.raw(), b.raw(), c.raw(), d.raw()