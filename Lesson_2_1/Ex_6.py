import chardet

with open("test_file.txt", 'w') as fo_obj:
    fo_obj.write('сетевое программирование')
    fo_obj.write('\nсокет')
    fo_obj.write('\nдекоратор')
    fo_obj.close()

with open("test_file.txt", "rb") as file:
    rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']
    print(encoding)

# При принудительном открытии в кодировке UTF-8 возникает исключение
# для корректной работы надо закоменнтировать код ниже
with open("test_file.txt", "rb") as f:
    contents = f.read().decode("utf-8")
    print(contents)
