new_list = [1, 2.2, 'lul', True, [1, 2, 3], (1, 2, 3), {'sad', 'kek'}, {'key1': 1, 'key2': 'value2'}]
for i in new_list:
    print('Тип элемента {} = {}'.format(i, str(type(i)).split("'")[1]))
