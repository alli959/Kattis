import sys
import collections

length = int(sys.stdin.readline().strip())

for i in range(length):
    action = sys.stdin.readline().strip()
    numberlength = int(sys.stdin.readline().strip())
    strnumbers = sys.stdin.readline().strip()
    strnumbers = strnumbers[1:-1]

    lister = collections.deque(strnumbers.split(','))
    left = True
    error = False
    for j in action:
        if j == 'R':
            if left:
                left = False
            else:
                left = True
        else:
            if numberlength == 0:
                error = True
                break
            numberlength -= 1
            if left:    
                lister.popleft()
            else:
                lister.pop()
    if error:
        print("error")
    else:
        counter = action.count('R')
        if counter%2 != 0:
            lister.reverse()
        

        print('[' + ','.join(lister) + ']')