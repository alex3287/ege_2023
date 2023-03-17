# Пробник вариант №3

A = [str(i) for i in range(100)]
B = ['0' + str(i) for i in range(10)]
E = ['']+A+B

D = [] # для сортировки
for i in range(10):
    for j in E:
        number = int(f'12{i}3{j}46')
        if number % 129 == 0:
            D.append((number, number // 129)) # для сортировки
D.sort() # для сортировки
for i in D: # для сортировки
    print(i) # для сортировки

