A = [int(i) for i in open('17.txt')]
print(A)
count = 0
max_sum = 0

for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        if A[i] % 160 != A[j] % 160:
            if A[i] % 7 == 0 or A[j] % 7 == 0:
                count += 1
                max_sum = max(max_sum, A[i]+A[j])

print(count, max_sum)