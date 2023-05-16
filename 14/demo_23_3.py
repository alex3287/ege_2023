# из 10-ой в любую другую
ABC = '0123456789ABCDEFG'
def ten_to_q(number, base):
    result = ''
    while number > 0:
        digit =  number % base
        result = ABC[digit] + result
        number //= base
    return result


# print(ten_to_q(255, 16))

# из любой в 10-ю с помощью int('число', СС)
# print(int('2342', 7))

ABC2 = '0123456789ABCDE'
for x in ABC2:
    first = f'123{x}5'
    second = '1{}233'.format(x)
    suma = int(first, 15) + int(second, 15)
    if suma % 14 == 0:
        print(x, suma // 14)