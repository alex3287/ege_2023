with open('input.txt') as fin:
    s = fin.readline()
# print(s)
s1 = s.replace('FE', '+')
s2 = s.replace('EF', '#')
print(s1)
# print(s2)

for n in range(1, 100):
    t1= '+' * n
    t2= '#' * n

    if t1 in s1:
        print(n, 'Ok')


    if t2 in s2:
        print(n, 'Ok')

