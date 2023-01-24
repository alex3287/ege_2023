s = '8' * 125

while '333' in s or '888' in s:
    if '333' in s:
        s = s.replace('333', '8', 1)
    else:
        s = s.replace('888', '3', 1)

print(s)