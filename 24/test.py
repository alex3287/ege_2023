s = 'CuFCuCFFeIC'
A = []
for i in range(len(s)-1):
    if s[i] == s[i].lower():
        continue
    elif s[i+1] == s[i+1].lower():
        A.append(s[i]+s[i+1])
    else:
        A.append(s[i])

print(A)
