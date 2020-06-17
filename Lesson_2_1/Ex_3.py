words = ['attribute', 'класс', 'функция', 'type']
for i in words:
    try:
        print(i.encode('ascii'))
    except UnicodeEncodeError:
        print('Слово не может быть записано в бинарном виде')
