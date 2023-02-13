A = [int(i) for i in open('input.txt')]

count = 0
sum_max = -1000000

for i in range(len(A)-1):
    if A[i] * A[i+1] % 3 == 0:
        count += 1
        sum_max = max(sum_max, (A[i]+A[i+1]))

print(count, sum_max)
