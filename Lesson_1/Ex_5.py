fin_revenue = float(input('Введите величину выручки: '))
fin_costs = float(input('Введите величину издержек: '))
if fin_revenue == fin_costs:
    print('Выручка равна издержкам')
elif fin_revenue < fin_costs:
    print('Издержки больше выручки')
else:
    print('Выручка больше издержек')
    profit_margin = 100 * (fin_revenue - fin_costs) / fin_revenue
    print('Рентабельность выручки: ', profit_margin, '%')
    staff_count = int(input('Введите количество сотрудников: '))
    profit_margin_per_emp = (fin_revenue - fin_costs) / staff_count
    print('Прибыль на одного сотрудника составила: ', profit_margin_per_emp)
