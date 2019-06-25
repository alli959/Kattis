import sys
length = int(sys.stdin.readline().strip())

def getTwo(string):
    return string[0:2]


while length != 0:
    arr = []

    for i in range(length):

        string = sys.stdin.readline().strip()
        arr.append(string)

    
    arr.sort(key = getTwo)
    
    for i in range(len(arr)):
        print(arr[i])
    print('')
    length = int(sys.stdin.readline().strip())
    
