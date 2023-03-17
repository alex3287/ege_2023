def devisions(number):
    maxi = 0
    if number**0.25 == int(number**0.25):
        count = 1
        maxi = 1
        for i in range(2, int(number**0.5)-1):
            if number % i == 0:
                count +=2
                maxi = number // i
        if count == 3:
            return maxi
        else:
            return 0
    return 0


for i in range(123_456_789, 223_456_789):
    A = devisions(i)
    if A:
        print(i, A)
