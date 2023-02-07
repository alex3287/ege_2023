number = 5*216**155 + 4*36**156 - 4*6**157 - 2023

count = 0
while number:
    if number % 6 == 0:
        count += 1
    number //= 6

print(count)
