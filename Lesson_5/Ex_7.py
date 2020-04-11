import json

comp_margin = {}
average_profit = {}
result_list = [comp_margin, average_profit]
comp_count = 0
sum_profit = 0
try:
    with open("Ex_7.txt") as f_obj:
        for line in f_obj:
            comp_margin[line.split()[0]] = float(line.split()[2]) - float(line.split()[3])
            if float(line.split()[2]) - float(line.split()[3]) > 0:
                comp_count += 1
                sum_profit += float(line.split()[2]) - float(line.split()[3])
except IOError:
    print("Произошла ошибка ввода-вывода!")
average_profit['average_profit'] = sum_profit / comp_count
json_string = json.dumps(result_list)
try:
    with open("Ex_7_output.txt", 'w') as fo_obj:
        fo_obj.write(json_string)
except IOError:
    print("Произошла ошибка ввода-вывода!")
