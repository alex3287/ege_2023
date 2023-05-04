def check_up(number):
    s = str(number)
    for i in range(len(s)-1):
        if int(s[i]) >= int(s[i+1]):
            return False
    return True


def check_down(number):
    s = str(number)
    for i in range(len(s) - 1):
        if int(s[i]) <= int(s[i + 1]):
            return False
    return True


def sum_digits(number):
    return sum(map(int, str(number)))


A = [int(i) for i in open('17.txt')]
# print(A)
count = 0
sum_mini = 1000_000
mini = min(i for i in A if check_down(i))
sum_digid = sum_digits(mini)
for i in range(len(A)-1):
    if (check_up(A[i]) and not (check_up(A[i+1]))
        or check_up(A[i+1]) and not (check_up(A[i]))):
        if A[i] * A[i+1] % sum_digid == 0:
            count += 1
            sum_mini = min(sum_mini, A[i] + A[i+1])

print(count, sum_mini)