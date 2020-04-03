try:
    user_input = int(input('Пожалуйста введите порядковый номер месяца: '))
    user_calendar = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
    if user_input in range(1, 13):
        for i_keys, i_values in user_calendar.items():
            if user_input in i_values:
                print('Время года:', i_keys)
    else:
        print('Введите корректный месяц')
except ValueError:
    print('Введите корректный месяц')
