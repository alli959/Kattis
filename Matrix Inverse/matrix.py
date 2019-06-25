import sys

caseNr = 1
for i in range(5):
    breakline = ""
    if i != 0:
        breakline = sys.stdin.readline().strip()
    
    first = sys.stdin.readline().strip()
    if len(first) == 0:
        break
    second = sys.stdin.readline().strip()
    firstarr = first.split(' ')
    secondarr = second.split(' ')
    ad = int(firstarr[0]) * int(secondarr[1])
    bc = int(firstarr[1]) * int(secondarr[0])
    under = ad - bc
    multipl = 1/under
    a = multipl * int(firstarr[0])
    b = 0 - (multipl * int(firstarr[1]))
    c = 0 - (multipl * int(secondarr[0]))
    d = multipl * int(secondarr[1])
    print("Case " + str(caseNr) + ":")
    print(str(int(d)) + " " + str(int(b))) 
    print(str(int(c)) + " " + str(int(a)))
    caseNr += 1