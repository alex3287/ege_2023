def is_prime(number):
    k = 2
    while number % k != 0 and k*k < number:
        k += 1
    return k*k > number

for i in range(20):
    n = i
    s = '>' + '0'*9 + '2'*30 + '1'*n + '0'*30 + '2'*9

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    suma = s.count('1') + s.count('2') * 2
    if is_prime(suma) == True:
        print(n)
        break
