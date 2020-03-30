user_input = abs(int(input('Введите число: ')))
greatest_digit = 0
while user_input:
    trail_digit = user_input % 10
    if trail_digit > greatest_digit:
        greatest_digit = trail_digit
    user_input = user_input // 10
print(greatest_digit)
