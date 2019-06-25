import sys

def number(stri):
    number = 0
    if "," in stri:
        list = stri.split(",")
        power = len(list) - 1
        for i in list:
            if i != "":
                number += (60 ** power) * int(i)
            power-= 1
    else:
        number = int(stri)
    return number

length = sys.stdin.readline().strip()
for i in range(int(length)):
    line = sys.stdin.readline().strip()
    print(number(line))
        
