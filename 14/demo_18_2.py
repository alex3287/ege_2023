ABC = '0123456789abcde'

for x in ABC:
    num_1 = f'123{x}5'
    num_2 = '1{}233'.format(x)
    suma = int(num_1, 15) + int(num_2, 15)
    if suma % 14 == 0:
        print(suma // 14)


