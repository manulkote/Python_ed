init_set = [2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 6, 6, 8, 8, 7, 7, 9, 9]
user_input = int(input('Введите число: '))
init_set.sort(reverse=True)
for i_ind, i_val in enumerate(init_set):
    if user_input > i_val:
        init_set.insert(i_ind, user_input)
        break
else:
    init_set.append(user_input)
print(init_set)
