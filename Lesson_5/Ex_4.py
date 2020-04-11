digits = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
try:
    fi_obj = open("Ex_4_File.txt")
    fo_obj = open("Ex_4_File_output.txt", 'w')
    for line in fi_obj:
        fo_obj.write(line.replace(line.split(' - ')[0], digits.get(int(line.split(' - ')[1]))))
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    fi_obj.close()
    fo_obj.close()
