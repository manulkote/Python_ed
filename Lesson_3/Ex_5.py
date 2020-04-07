resulting_sum = 0
running = 'true'
while running == 'true':
    user_input = input('Введите строку чисел разделенных пробелом: ')
    numbers = user_input.split()
    for item in numbers:
        if item == 'q':
            running = 'false'
            break
        else:
            resulting_sum = resulting_sum + int(item)
    print('Итоговая сумма:', resulting_sum)
