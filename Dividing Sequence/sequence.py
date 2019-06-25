import sys
number = int(sys.stdin.readline().strip())

arr = []
value = 1
while value <= number:
    arr.append(value)
    value *=2

print(len(arr))

print(' '.join(str(i) for i in arr))



    
