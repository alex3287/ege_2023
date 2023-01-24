abc = '0123456789abcdef'
def ten_to_q(number, base):
    count = 0
    while number > 0:
        if number % base == 6:
            count += 1
        number //= base
    return count


number = 49**10 + 7**30 - 49
print(number)
print(ten_to_q(number, 7))