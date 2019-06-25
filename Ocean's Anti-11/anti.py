import sys
import math
length = int(sys.stdin.readline().strip())

largest = (10**9) + 7

for i in range(length):

    fib1 = 1
    fib2 = 1    
    value = int(sys.stdin.readline().strip())

    for i in range(value):
        temp = fib1
        fib1 += fib2
        fib2 = temp



    print(fib1%largest)
