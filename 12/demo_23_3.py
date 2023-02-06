def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


for i in range(50):
    n = i
    s = '>' + '0'*39 + '1'*n + '2'*39

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    suma = s.count('1') + s.count('2')*2

    if is_prime(suma) == True:
        print(n, suma)


