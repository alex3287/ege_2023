def deviders(number):
    maxi = 0
    count = 1
    for i in range(2, int(number**0.5)):
        if number % i == 0:
            count += 2
            maxi = max(maxi, number//i)
    if count == 3:
        return maxi
    return 0


for i in range(123_456_789, 223_456_789):
    if int(i**0.5) == i**0.5:
        A = deviders(i)
        if A:
            print(i, A)
