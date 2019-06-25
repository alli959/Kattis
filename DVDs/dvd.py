import sys

def sortarr(arr, largest):
    position = 1
    for i in arr:
        if int(i) == position:
            position += 1
    return position


length = int(sys.stdin.readline().strip())
for i in range(length):
    largest = int(sys.stdin.readline().strip())
    values = sys.stdin.readline().strip()
    arr = values.split(' ')
    print(largest - (sortarr(arr,largest)) +1)


