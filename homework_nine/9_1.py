import time


class TrafficLight:
    __color = ['Красный','Желтый','Зеленый']

    def running(self):
        while True:
            print(f'Цвет светофора {TrafficLight.__color[0]}')
            time.sleep(7)
            print(f'Цвет светофора {TrafficLight.__color[1]}')
            time.sleep(2)
            print(f'Цвет светофора {TrafficLight.__color[2]}')
            a = input('Введите 1 если едем дальше и 2 если пододжем еще')
            if a == '1':
                break
            time.sleep(5)



a = TrafficLight()
a.running()