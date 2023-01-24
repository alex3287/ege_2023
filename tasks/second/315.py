# a ^ x; 2 ^ 10 = 1024
a = int(input())
x = int(input())
f = 1

for i in range(x):
    f *= a

print(f)


