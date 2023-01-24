abc = '0123456789abcde'

for x in abc:
    s1 = f'123{x}5'
    s2 = '1{}233'.format(x)
    suma = int(s1, 15) + int(s2, 15)
    if suma % 14 == 0:
        print(s1, s2, suma / 14)
