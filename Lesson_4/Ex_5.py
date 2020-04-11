from functools import reduce


def my_multiply(a, b):
    x = a * b
    return x


new_list = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(my_multiply, new_list))
