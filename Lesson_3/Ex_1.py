def my_func(number_1, number_2):
    try:
        res = float(number_1) / float(number_2)
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
    return res


x = my_func(input('Введите первое число '), input('Введите второе число '))
print(x)
