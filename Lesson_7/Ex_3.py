class Cell:
    def __init__(self, cellule):
        self.cellule = cellule
        self.order = ''

    def __add__(self, other):
        return Cell(self.cellule + other.cellule)

    def __sub__(self, other):
        if self.cellule > other.cellule:
            return Cell(self.cellule - other.cellule)
        else:
            print('Разность клеток должна быть больше 0')

    def __mul__(self, other):
        return Cell(self.cellule * other.cellule)

    def __truediv__(self, other):
        return Cell(self.cellule // other.cellule)

    def make_order(self, cells_in_row):
        self.order = ('*' * cells_in_row + '\n') * (self.cellule // cells_in_row) + '*' * (self.cellule % cells_in_row)
        return self.order


a = Cell(7)
b = Cell(5)
c = a * b
print(c.cellule)
print(c.make_order(10))