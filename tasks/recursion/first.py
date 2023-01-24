def sum_digits_number(number):
    if number < 10:
        return number
    return number % 10 + sum_digits_number(number // 10)


print(sum_digits_number(4456))