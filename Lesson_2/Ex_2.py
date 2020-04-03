user_list = []
swapped_list = []
while True:
    next_item = input("Введите новый элемент списка или 'end' для завершения ")
    if next_item == 'end':
        break
    else:
        user_list.append(next_item)
        continue
while user_list:
    try:
        swapped_list.append(user_list.pop(1))
        swapped_list.append(user_list.pop(0))
    except IndexError:
        swapped_list.append(user_list.pop(0))
print(swapped_list)
