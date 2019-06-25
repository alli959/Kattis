import sys

x = int(sys.stdin.readline().strip())

y = int(sys.stdin.readline().strip())

if x < 0:
    if y<0:
        print(3)
    else:
        print(2)
else:
    if y<0:
        print(4)
    else:
        print(1)

