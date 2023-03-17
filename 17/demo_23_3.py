# считываем данные из файла
A = [int(i) for i in open('17.txt')]
print(A)

count = 0
max_3 = -100_000
max_sum = 0

# находим максимальное оканчивающееся на 3
# и возводим его в квадрат
# max_3 = max(i for i in A if abs(i) % 10 == 3)
for i in A:
    if abs(i) % 10 == 3:
        max_3 = max(max_3, i)
max_3 = max_3**2

# основные проверки
for i in range(len(A)-1):
    suma = A[i]**2 + A[i+1]*A[i+1]
    if abs(A[i]) % 10 == 3 and abs(A[i+1]) % 10 != 3 and suma >= max_3:
        count += 1
        max_sum = max(max_sum, suma)
    elif abs(A[i]) % 10 != 3 and abs(A[i+1]) % 10 == 3 and suma >= max_3:
        count += 1
        if suma > max_sum:
            max_sum = suma

print(count, max_sum)