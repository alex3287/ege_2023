A = [str(i) for i in range(1000)]
B = ['0' + str(i) for i in range(100)]
C = ['00' + str(i) for i in range(10)]
E = ['']+A+B+C


for i in range(10):
    for j in E:
        number = int(f'1{i}2139{j}4')
        if number % 2023 == 0:
            print(number, number // 2023)




