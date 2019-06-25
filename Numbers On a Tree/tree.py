import sys

import collections
string = sys.stdin.readline().strip()

arr = string.split(' ')

length = int(arr[0])





def maxPosValue(size, length, nextSum, stop):
    
    if length >= stop:

        size = size + nextSum
        nextSum = nextSum/2
        return maxPosValue(size, length-1, nextSum, stop)
    else:
        return int(size)



def valueFind(position, number, direction):
        if len(direction) == 0:
                return number
        if direction[0] == 'L':
                number -= position
                position *= 2
        else:
                number -= position
                number -= 1
                position *= 2
                position += 1
        direction.popleft()
        return valueFind(position, number, direction)
        



        

maxNumber = 2
for i in range(length-1):
        maxNumber = maxNumber*2
if len(arr)!=1:
        direction = arr[1]

        stop = len(direction)



        rootNumber = maxPosValue(0, length, maxNumber, 1 )

        rootNumber += 1
        
        lister = collections.deque(direction)

        value = valueFind(1, rootNumber, lister)

        print(value)


else:
        maxRowNumber = maxPosValue(0, length, maxNumber, 0 )
        print(maxRowNumber)







