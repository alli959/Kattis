import sys
import math


length = int(sys.stdin.readline().strip())

for i in range(length):
    size = int(sys.stdin.readline().strip())
    xPos = 0
    yPos = 0
    rot = 0
    for j in range(size):
        string = sys.stdin.readline().strip()
        array = string.split(' ')
        rot += float(array[0]) % 360
        distance = float(array[1])
        xPos += distance * math.sin(-rot * math.pi/180)
        yPos += distance * math.cos(-rot * math.pi/180)
    print(str(xPos) + " " + str(yPos))


