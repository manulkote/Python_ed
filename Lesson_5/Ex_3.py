salary_average = 0
staff_count = 0
try:
    f_obj = open("Ex_3_File.txt")
    for line in f_obj:
        salary_average += float(line.split()[1])
        staff_count += 1
        if float(line.split()[1]) < 20000:
            print(line.split()[0], 'имеет оклад ниже 20000')
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f_obj.close()
print('Средний доход:', round(salary_average / staff_count, 2))
