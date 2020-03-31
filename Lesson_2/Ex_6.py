goods_struct = []
goods_dict = {}
while True:
    new_item_number = input("Введите номер товара или 'end' для завершения формирования структуры товаров ")
    new_item_params = {}
    if new_item_number == 'end':
        break
    else:
        while True:
            new_item_att = input("Введите параметр товара или 'end' для завершения формирования товара ")
            if new_item_att == 'end':
                break
            else:
                new_item_att_val = input('Введите величину параметра ')
            new_item_params[new_item_att] = new_item_att_val
    goods_struct.append((new_item_number, new_item_params))
print(goods_struct)
for i in goods_struct:
    for k, j in i[1].items():
        if k in goods_dict.keys():
            goods_dict[k].append(j)
        else:
            goods_dict[k] = [j]
print(goods_dict)