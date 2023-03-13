number = 4**511 + 2**511 - 511

count = 0
while number:
    if number % 2 == 1:
        count += 1
    number //= 2

print(count)
