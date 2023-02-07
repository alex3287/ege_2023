def F(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return 11*n + F(n-1)
    return 11*F(n-2) + n


suma = 0
for n in range(35, 51):
    result = F(n)
    if result % 2 == 0:
        suma += result

print(suma)
print(len(str(suma)))