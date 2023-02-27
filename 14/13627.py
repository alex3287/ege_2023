def ten_to_q(number, base):
    count = 0
    while number > 0:
        if number % base == 1:
            count += 1
        number //= base
    return count


number = 4**511 + 2**511 - 511
number2 = number

count = 0
while number > 0:
    if number % 2 == 1:
        count += 1
    number //= 2

print(count)
print(ten_to_q(number2, 2))