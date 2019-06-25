import sys
import math

largest = (10**9) + 7



length = int(sys.stdin.readline().strip())

for i in range(length):
    size = int(sys.stdin.readline().strip()) - 1
    value = 8 * pow(9,size,largest)
    print(value%largest)

    