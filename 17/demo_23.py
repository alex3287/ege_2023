A = [int(i) for i in open('input.txt')]

count = 0
sum_max = 0
item_3 = -10000
item_square = 0

for i in A:
    if abs(i) % 10 == 3 and i > item_3:
        item_3 = i
        item_square = i**2

for i in range(len(A)-1):
    temp = A[i]**2 + A[i+1]**2
    if ((abs(A[i]) % 10 == 3 and abs(A[i+1]) % 10 != 3) or
            (abs(A[i]) % 10 != 3 and abs(A[i+1]) % 10 == 3)):
        if temp >= item_square:
            count += 1
            sum_max = max(sum_max, temp)

print(count, sum_max)
