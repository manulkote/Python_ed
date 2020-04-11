f_obj = open("Ex_1_File.txt", 'w')
while True:
    new_line = input('Введите новую строчку или пустую строку для завершения... ')
    if new_line == '':
        f_obj.close()
        break
    else:
        f_obj.write(new_line + '\n')
