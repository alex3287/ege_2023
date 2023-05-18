ABC = '0123456'
def ten_to_seven(number):
    if number < 7:
        return ABC[number]
    return ten_to_seven(number//7) + ABC[number%7]


number_7 = ten_to_seven(234)
print(number_7, int(number_7, 7) % 10)

# number = 5*343**8 + 4*49**12 + 7**14 - 98
# print(ten_to_seven(number))
# # 0770
# # 00001001
# number = 123
