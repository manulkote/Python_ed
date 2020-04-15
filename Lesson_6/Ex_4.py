class Car:
    def __init__(self, c_speed, c_color, c_name):
        self.speed = c_speed
        self.color = c_color
        self.name = c_name
        self.is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, t_direction):
        print('Машина повернула в', t_direction)

    def show_speed(self):
        print('Текущая скорость', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Текущая скорость', self.speed, 'скорость превышена')
        else:
            print('Текущая скорость', self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Текущая скорость', self.speed, 'скорость превышена')
        else:
            print('Текущая скорость', self.speed)


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, c_speed, c_color, c_name):
        super().__init__(c_speed, c_color, c_name)
        self.is_police = True


car_1 = TownCar(70, 'Red', 'Audi')
car_2 = WorkCar(50, 'Green', 'Bentley')
car_3 = SportCar(180, 'White', 'ZAZ')
car_4 = PoliceCar(90, 'Blue', 'Ford')
car_1.go()
car_1.turn('Left')
car_1.stop()
print(car_1.speed, car_1.color, car_1.name, car_1.is_police)
print(car_2.speed, car_2.color, car_2.name, car_2.is_police)
print(car_3.speed, car_3.color, car_3.name, car_3.is_police)
print(car_4.speed, car_4.color, car_4.name, car_4.is_police)
car_1.show_speed()
car_2.show_speed()
