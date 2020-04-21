class Matrix:
    def __init__(self, *args):
        self.m_body = [line for line in args]

    def __str__(self):
        return '\n'.join([' '.join([str(k) for k in i]) for i in self.m_body])

    def __add__(self, s_matrix):
        return Matrix(*[list(sum(y) for y in zip(*x)) for x in zip(self.m_body, s_matrix.m_body)])


a = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(a)
print(type(a))
b = Matrix([6, 5, 4], [3, 2, 1], [1, 2, 3])
print(b)
print(type(b))
c = a + b
print(c)
print(type(c))
