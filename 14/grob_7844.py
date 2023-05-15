import string


s = string.ascii_uppercase
ABC = '0123456789' + s
for x in ABC:
    for p in range(2, 37):
        for q in range(2, 37):
            try:
                suma = int(f'ALE{x}', p) + int('DANOV', q)
            except:
                pass
            if suma % 2023 == 0:
                print(x, suma // 2023)

# k = int('123', 36)
# print(ABC, len(ABC), ABC.find('V'), ABC.find('L'))
# print(int('DANOV', 34))