import csv
import re


def get_data(*args):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [os_prod_list, os_name_list, os_code_list, os_type_list]
    for x in args:
        with open(x) as f_n:
            for el_str in f_n:
                reg_prod_list = re.match('Изготовитель системы:(\s+)(.+)',
                                         el_str)
                reg_name_list = re.match('Название ОС:(\s+)(.+)', el_str)
                reg_code_list = re.match('Код продукта:(\s+)(.+)', el_str)
                reg_type_list = re.match('Тип системы:(\s+)(.+)', el_str)
                if reg_prod_list:
                    os_prod_list.append(reg_prod_list.group(2))
                elif reg_name_list:
                    os_name_list.append(reg_name_list.group(2))
                elif reg_code_list:
                    os_code_list.append(reg_code_list.group(2))
                elif reg_type_list:
                    os_type_list.append(reg_type_list.group(2))
    return main_data


def write_to_csv(arg_1):
    with open(arg_1, 'w', newline='') as f_n:
        f_n_writer = csv.writer(f_n)
        data = get_data('info_1.txt', 'info_2.txt', 'info_3.txt')
        for row in data:
            f_n_writer.writerow(row)


write_to_csv('main_data.csv')
