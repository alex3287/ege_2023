number = 5*216**1255 + 4*36**1256 - 4*6**1257 - 2023

count = 0
while number:
    if number % 6 == 5:
        count += 1
    number //= 6

print(count)
