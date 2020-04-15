class Road:
    def __init__(self, r_length, r_width):
        self._length = r_length
        self._width = r_width
        self._height = 5
        self._kilos = 25

    def mass_calc(self):
        print('Для покрытия дороги асфальтом необходимо:',
              self._length * self._width * self._height * self._kilos / 1000, 'т')


r = Road(20, 5000)
r.mass_calc()
