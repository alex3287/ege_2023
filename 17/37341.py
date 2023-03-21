A = [int(i) for i in open('17.txt')]
print(A)

count = 0
max_sum = 0

for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        # print(A[i], A[j], '->', A[i]*A[j] / 26)
        if (A[i] * A[j]) % 26 == 0:
            count += 1
            max_sum = max(max_sum, A[i]+A[j])

print(count, max_sum)