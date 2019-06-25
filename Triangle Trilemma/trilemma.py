import sys
import math
length = int(sys.stdin.readline().strip())
EPS = 1e-9


def distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2


def checkcoll(string):
    arr = string.split(' ')
    x1 = int(arr[0])
    y1 = int(arr[1])
    x2 = int(arr[2])
    y2 = int(arr[3])
    x3 = int(arr[4])
    y3 = int(arr[5])

    position = 0.5*((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1))

    if position == 0:
        return False
    return True

def checkH(ab,c):
    return math.fabs(c-ab) < EPS



def lengths(string):
    if not checkcoll(string):
        return "not a triangle", []
    arr = string.split(' ')
    A =  distance(int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3]))
    B = distance(int(arr[2]), int(arr[3]),int(arr[4]), int(arr[5]))
    C = distance(int(arr[4]), int(arr[5]),int(arr[0]), int(arr[1]))
    arr = [A,B,C]

    if A == B or A == C or B == C:
        return "isosceles", arr
    else:
        return "scalene", arr

for i in range(length):
    string = sys.stdin.readline().strip()
    ltype,arr = lengths(string)
    if len(arr) == 0:
        print("Case #" + str(i+1) + ": " + ltype)
    else:
        arr.sort()
        AB = arr[0] + arr[1]
        if checkH(AB,arr[2]):
            print("Case #" + str(i+1) + ": " + ltype + " right triangle")

        elif arr[2] < arr[0] + arr[1]:
            print("Case #" + str(i+1) + ": " + ltype + " acute triangle") 

        else:
            print("Case #" + str(i+1) + ": " + ltype + " obtuse triangle")
            

