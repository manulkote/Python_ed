class Worker:
    def __init__(self, w_name, w_surname, w_position, w_wage, w_bonus):
        self.name = w_name
        self.surname = w_surname
        self.position = w_position
        self._income = {'wage': w_wage, 'bonus': w_bonus}


class Position(Worker):
    def get_full_name(self):
        print('Полное имя сотрудника:', self.surname, self.name)

    def get_total_income(self):
        print('Доход с учетом премии:', self._income['wage'] + self._income['bonus'])


pos1 = Position('Иван', 'Иванов', 'Риэлтор', 30000, 60000)
print(pos1.name, pos1.surname, pos1.position, pos1._income)
pos1.get_full_name()
pos1.get_total_income()

pos2 = Position('Петр', 'Петров', 'Инженер', 20000, 8000)
print(pos2.name, pos2.surname, pos2.position, pos2._income)
pos2.get_full_name()
pos2.get_total_income()
