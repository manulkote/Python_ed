from sys import argv


def calc_salary(a, b, c):
    x = (a * b) + (a * b * c / 100)
    return x


y = calc_salary(float(argv[1]), float(argv[2]), float(argv[3]))
print('Зарплата за {} часов по ставке {} в час с учетом премии в {} процентов составляет {}'.format(argv[1], argv[2],
                                                                                                    argv[3], y))
