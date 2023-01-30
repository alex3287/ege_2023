def ten_to_q(number, base):
    count = 0
    while number:
        digit = number % base
        if digit == 0:
            count += 1
        number //= base
    return count


number = 3*4**38 + 2*4**23 + 4**20 + 3*4**5 + 2*4**4 + 1
print(number)
print(ten_to_q(number, 16))

