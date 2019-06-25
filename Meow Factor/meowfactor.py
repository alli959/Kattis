import sys
number = int(sys.stdin.readline().strip())
isNone = True
tester = int(number**(1/9.0)) + 1

for i in range(tester,0,-1):
        if number % i**9 == 0:
                isNone = False
                print(i)
                break

if(isNone):
        print(1)

