import sys
import collections
string = sys.stdin.readline().strip()
lister = collections.deque()

for i in string:
    if i != '<':
        lister.append(i)
    else:
        lister.pop()
print(''.join(lister))





            