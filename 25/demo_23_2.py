from fnmatch import *

for x in range(1,10**10+1, 2023):
    if fnmatch(str(x),'1?2139*4'):
        print(x,x // 2023)
