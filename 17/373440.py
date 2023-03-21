A = [int(i) for i in open('17.txt')]
print(A)

max_sum = 0
count = 0

for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        # print(A[i], A[j])
        if (A[i]-A[j]) % 2 == 0 and (A[i] % 31 == 0 or A[j] % 31 == 0):
            count += 1
            max_sum = max(max_sum, A[i]+A[j])

print(count, max_sum)