import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_json = {'item': item,
                 'quantity': quantity,
                 'price': price,
                 'buyer': buyer,
                 'date': date}
    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(dict_json, f_n, indent=4, ensure_ascii=False)


write_order_to_json('laptop', 1, '200$', 'Микрочелик', '06/18/2020')
