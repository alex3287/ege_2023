s = '>' + '1'*10 + '2'*20 + '3'*30
# s = '>' + '3'*10 + '1'*5 + '3'*10 + '2'*5 + '1'*5 + '3'*10 + '2'*15
# print(s)

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)

suma = s.count('1') + s.count('2') * 2
print(s)
print(suma)