user_input = int(input('Введите время в секундах: '))
calc_hours = user_input // 3600
calc_minutes = user_input % 3600 // 60
calc_seconds = user_input % 60
print('Введенное время составляет: {:02d}:{:02d}:{:02d}'.format(calc_hours, calc_minutes, calc_seconds))
