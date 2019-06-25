import sys
length = int(sys.stdin.readline().strip())

seq = sys.stdin.readline().strip()

li = list(seq)

mutation = 0
boole = True

for i in range(length-1, -1, -1):
    if boole:
        if li[i] != 'A':
            mutation += 1
            if li[i-1] == 'B':
                boole = False
    else:
        if li[i] != 'B':
            mutation += 1
            if li[i-1] == 'A':
                boole = True

print(mutation)
