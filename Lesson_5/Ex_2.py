words_count = 0
line_count = 0
try:
    f_obj = open("Ex_2_File.txt")
    for line in f_obj:
        words_count += len(line.split())
        line_count += 1
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f_obj.close()
print('Слов в файле:', words_count)
print('Строк в файле:', line_count)
