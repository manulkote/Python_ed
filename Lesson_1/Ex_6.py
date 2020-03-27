first_day_result = float(input('Введите результат в первый день: '))
deserved_result = float(input('Введите желаемый результат: '))
run_day = 1
while first_day_result < deserved_result:
    run_day = run_day + 1
    first_day_result = first_day_result * 1.1
print('Спортсмен достиг результата на', run_day, 'день')
