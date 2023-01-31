ABC = '0123456789abcde'

for x in ABC:
    first = f'123{x}5'
    second = '1{}233'.format(x)
    suma = int(first, 15) + int(second, 15)
    if suma % 14 == 0:
        print(x, suma // 14)

