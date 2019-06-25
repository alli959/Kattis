import sys
import math

length = int(sys.stdin.readline().strip())
maxNumber = 1000000000



def fibo(length):
    if length == 1:
        return 0,1
    midPoint = math.floor(length/2)
    tempPrev,tempCurrent = fibo(midPoint)
    tempCurrent = tempCurrent % maxNumber
    tempPrev = tempPrev % maxNumber
    current = (tempCurrent*(2* tempPrev + tempCurrent)) % maxNumber
    prev = (tempPrev**2 + tempCurrent**2) % maxNumber
    nextValue = (prev + current) % maxNumber
    if length % 2 == 0:
        return prev,current
    else:
        return current,nextValue



for i in range(length):
    string = sys.stdin.readline().strip()
    arr = string.split(' ')
    prev,number = fibo(int(arr[1]))
    print(arr[0]+" " + str(number))

    
    

