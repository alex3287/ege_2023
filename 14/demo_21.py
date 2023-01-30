def ten_to_q(number, base):
    result = 0
    while number > 0:
        digit = number % base
        if digit == 6:
            result += 1
        number //= base
    return result


number = 49**7 + 7**21 -7
print(number)
print(ten_to_q(number, 7))

