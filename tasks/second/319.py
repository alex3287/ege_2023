a = float(input())
n = int(input())
p = a
summ = 1
for i in range(n):
    summ += p
    p = p * a

print(summ)
# 1 + 2 + 4 + 8