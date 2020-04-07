def my_capitalize(lower_string):
    return lower_string.capitalize()


user_input = input('Введите слова разделенные пробелом: ').split()
user_output = list(map(my_capitalize, user_input))
user_text = ' '
print(user_text.join(user_output))
