A = [int(i) for i in open('17.txt')]
print(A)
count = 0
max_sum = -20_000

for i in range(len(A)-1):
    if (A[i] * A[i+1]) % 3 == 0:
        count += 1
        max_sum = max(max_sum, A[i] + A[i+1])

print(count, max_sum)