# 273x2_158 + 1x390_158
def q158_to_ten(number):
    k = len(number)-1
    result = 0
    for i in number:
        result += i * 158**k
        k -= 1
    return result

result = 0
for x in range(158):
    first = [2, 7, 3, x, 2]
    second = [1, x, 3, 9, 0]
    dec_first = q158_to_ten(first)
    dec_second = q158_to_ten(second)
    suma = dec_first + dec_second

    if suma % 73 == 0:
        print(x, suma // 73)
        result += suma // 73

print(result)

# 273-123-2