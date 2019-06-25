import sys

tests = int(sys.stdin.readline().strip())
for i in range(tests):
    inpstr = sys.stdin.readline().strip()
    inparr = inpstr.split(' ')
    cities = int(inparr[0])
    pilots = int(inparr[1])
    print(cities-1)
    for j in range(pilots):
        value = sys.stdin.readline().strip()
