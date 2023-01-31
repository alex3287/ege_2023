# перевод из любой системы счисления в десятичную
number_2 = '10100'
number_5 = '1201234'
number_16 = 'ff'

# print(int(number_16, 16))
# print(oct(255))

# перевод из десятичной системы счисления в любую
ABC = '0123456789abcdefgh'
def ten_to_q(number, base):
    result = ''
    while number > 0:
        digit = number % base
        result = ABC[digit] + result
        number //= base
    return result


print(ten_to_q(255, 16))

ABC = '0123456789abcdefgh'
def ten_to_q2(number, base):
    if number < base:
        return ABC[number]
    return ten_to_q2(number // base, base) + ABC[number % base]



