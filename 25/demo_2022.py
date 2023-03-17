def find_M(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return i + number // i
    return 0


for i in range(700_000, 1000_000_000):
    M = find_M(i)
    if M % 10 == 8:
        print(i, M)

# 36 -> 2, 3, 4, 6,   6, 9, 12, 18 ===
# 47 -> 2, 3, 4, 5, 6,
# 17 -> 2, 3, 4
# 25 -> 5 5
