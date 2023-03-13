# считываем числа из файла (числа в файле в строках)
A = [int(i) for i in open('17.txt')]
# print(A)

# находим максимальное число оканчивающееся на 3
# и возводим его в квадрат
max_3 = -3333333
for i in A:
    if abs(i) % 10 == 3:
        max_3 = max(i, max_3)
max_3_sqr = max_3 * max_3

# находим количестов подходящих пар
count = 0
max_sum = 0
for i in range(len(A)-1):
    suma = A[i]*A[i] + A[i+1]**2
    if abs(A[i]) % 10 == 3 and abs(A[i+1]) % 10 != 3 and suma >= max_3_sqr:
        count += 1
        max_sum = max(max_sum, suma)
    elif abs(A[i]) % 10 != 3 and abs(A[i+1]) % 10 == 3 and suma >= max_3_sqr:
        count += 1
        max_sum = max(max_sum, suma)

print(count, max_sum)