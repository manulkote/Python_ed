course_dict = {}
try:
    f_obj = open("Ex_6.txt")
    for line in f_obj:
        course_dict[line.split(':')[0]] = sum(
            [int(i.split('(')[0].replace('—', '0').replace('\n', '')) for i in line.split(':   ')[1].split('   ')])
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f_obj.close()
print(course_dict)
