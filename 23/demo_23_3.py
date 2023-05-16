# s = open('23.txt').read()
with open('24.txt') as fin:
    s = fin.read()
# print(s)

s = s.replace('D', 'F').replace('C', 'F')
s = s.replace('O', 'A')
s = s.replace('FA', '*')
print(s)
# template = '*' * 95
#
# if template in s:
#     print('Ok')
# else:
#     print('No')
for n in range(100):
    template = '*' * n
    if template in s:
        print(n, 'Ok')
    else:
        print(n, 'No')