# читаем файл
A = [int(i) for i in open('17.txt')]
print(A)

count = 0
max_sum = 0
max_3 = -10000

# находим максимальное оканчивающее на 3 и возводим в квадрат
for i in range(len(A)):
    if abs(A[i]) % 10 == 3 and A[i] > max_3:
        max_3 = A[i]
max_3 = max_3 ** 2

# ТОЛЬКО один элемент в паре оканчивается на 3
# сумма квадратов элементов >= квадрата максимального оканчивающегося на 3
for i in range(len(A)-1):
    suma = A[i]**2 + A[i+1]**2
    if abs(A[i]) % 10 == 3 and abs(A[i+1]) % 10 != 3 and suma >= max_3:
        count += 1
        max_sum = max(max_sum, suma)
    elif abs(A[i]) % 10 != 3 and abs(A[i+1]) % 10 == 3 and suma >= max_3:
        count += 1
        if suma > max_sum:
            max_sum = suma
print(count, max_sum)