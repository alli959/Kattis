import sys
import math

strvalue = sys.stdin.readline().strip()
arr = strvalue.split(' ')

while int(arr[0]) != 0:
    cube = int(arr[0])**3
    smallCube = 6*int(arr[1])/math.pi
    resultCube = cube - smallCube
    diameter = resultCube**(1/3)
    print(diameter)
    strvalue = sys.stdin.readline().strip()
    arr = strvalue.split(' ')


