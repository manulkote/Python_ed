def my_func(*, user_name, surname, year_of_birth, city, email, phone):
    return user_name, surname, year_of_birth, city, email, phone


x = my_func(user_name=input('Введите имя: '), surname=input('Введите фамилию: '),
            year_of_birth=input('Введите год рождения: '), city=input('Введите город проживания: '),
            email=input('Введите email: '), phone=input('Введите номер телефона: '))
print(
    'Имя: {0[0]}, Фамилия:{0[1]}, Год рождения: {0[2]}, Город проживания: {0[3]}, Email: {0[4]}, Тел.: {0[5]}'.format(
        x))
