class Stationery:
    def __init__(self, s_title):
        self.title = s_title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')


st_1 = Stationery('My_stationary')
st_1.draw()
st_2 = Pen('My_Pen')
st_2.draw()
st_3 = Pencil('My_Pencil')
st_3.draw()
st_4 = Handle('My_Handle')
st_4.draw()
