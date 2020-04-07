def my_func(arg_1, arg_2, arg_3):
    sums = [arg_1, arg_2, arg_3]
    sums.sort()
    return sums[1] + sums[2]


x = my_func(7, 4, 6)
print(x)
