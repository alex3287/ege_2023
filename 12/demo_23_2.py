def is_prime(number):
    k = 2
    while number % k != 0 and k*k < number:
        k += 1
    return k*k > number


# print(is_prime(25))
for i in range(1000_000, 1000_0000):
    if is_prime(i):
        print(i)

# 36 -> 2, 3, 4, 6, 6, 9, 12, 18
# 42 -> 2, 3, 6, 7, 14, 21
# 47 ->
# for i in range(50):
#     n = i
#     s = '>' + '0'*39 + '1'*n + '2'*39
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '1>', 1)
#
#     suma = s.count('1') + s.count('2') * 2
#     if is_prime(suma) == True:
#         print(n)
#         break