user_input = input('Введите строку разделенную пробелами: ')
user_split = user_input.split()
for i_idx, i_str in enumerate(user_split):
    print(str(i_idx)+'.', i_str[:10])
