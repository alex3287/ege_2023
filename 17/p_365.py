A = [int(i) for i in open('17.txt')]
count = 0
max_average = -100_000
mini = 100_000
maxi = -100_000
for i in range(len(A)-1):
    if (abs(A[i]) % 10 == 1 and abs(A[i+1]) % 10 != 1 or
            abs(A[i]) % 10 != 1 and abs(A[i + 1]) % 10 == 1):
        average = (A[i] + A[i+1]) / 2
        max_average = max(max_average, average)

for i in range(len(A)-1):
    if (abs(A[i]) % 10 == 1 and abs(A[i+1]) % 10 != 1 or
            abs(A[i]) % 10 != 1 and abs(A[i + 1]) % 10 == 1):
        if A[i] < max_average and A[i+1] < max_average:
            mini = min(mini, A[i], A[i+1])

for i in range(len(A)-1):
    if (abs(A[i]) % 10 == 1 and abs(A[i + 1]) % 10 != 1 or
            abs(A[i]) % 10 != 1 and abs(A[i + 1]) % 10 == 1):
        if A[i] < max_average and A[i+1] < max_average:
            count += 1
            if A[i] == mini or A[i+1] == mini:
                maxi = max(maxi, A[i], A[i+1])

print(count, maxi)
