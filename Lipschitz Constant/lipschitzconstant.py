import sys
import operator

length = int(sys.stdin.readline().strip())
values = []
for i in range(length):
    value = sys.stdin.readline().strip()
    values.append(value)
x = []
z = []
arr = []
for i in values:
    value = i.split(' ')
    arr.append(value)

arr.sort(key = operator.itemgetter(0, 1))
L = []

for i in arr:
        x.append(float(i[0]))
        z.append(float(i[1]))


for i in range(1,length):
        x1 = x[i-1]
        x2 = x[i]
        z1 = z[i-1]
        z2 = z[i]
        upper = abs(z1 - z2)
        lower = abs(x1-x2)
        value = upper/lower
        L.append(value)

returnvalue = 0

for i in L:
    if i > returnvalue:
        returnvalue = i
        
if (returnvalue).is_integer():
    print(int(returnvalue))
else:
    print(returnvalue)
