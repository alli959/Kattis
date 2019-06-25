import sys

isgood = "yes"
word = sys.stdin.readline().strip()

arr = word.split(' ')

dict = {}

for i in arr:
    if i in dict:
        isgood = "no"
        break
    else:
        dict[i] = 0

print(isgood)
    


