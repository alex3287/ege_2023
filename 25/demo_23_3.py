import fnmatch


for i in range(0, 10**10):
    if fnmatch.fnmatch(str(i), '1?2139*4') and i % 2023 == 0:
        print(i, i // 2023)



