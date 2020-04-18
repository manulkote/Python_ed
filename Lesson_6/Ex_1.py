import time


class TrafficLight:  # CamelStyle
    def __init__(self):
        self.__color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        while True:
            print('Сейчас светофор', self.__color[0])
            time.sleep(7)
            print('Сейчас светофор', self.__color[1])
            time.sleep(2)
            print('Сейчас светофор', self.__color[2])
            time.sleep(5)


f = TrafficLight()
f.running()
