def F(n):
    if n <= 1:
        return 1
    if n % 3 == 0:
        return 2*F(n-1) + F(n-2)
    return 3*F(n-2) + F(n-1)


def sum_digits_number(number):
    if number < 10:
        return number
    return number % 10 + sum_digits_number(number // 10)


def is_prime(number):
    if number == 1:
        return False
    k = 2
    while number % k != 0 and k*k < number:
        k += 1
    return k*k > number


count = 0
for i in range(1, 36):
    result = F(i)
    suma = sum_digits_number(result)
    if is_prime(suma):
        count += 1
        
print(count)