import sys
vect = []
for i in range(10000):
    str = sys.stdin.readline().strip()
    if str == '':
        break
    vect.append(str)

arr = []
for i in vect:
    v = i.split(' ')
    arr.append(v)


dict = {}

for i in arr:
    if i[0] == "define":
        dict[i[2]] = i[1]
    elif i[0] == "eval":
        if i[1] in dict and i[3] in dict:
            if i[2] == "<":
                if int(dict[i[1]]) < int(dict[i[3]]):
                    print("true")
                else:
                    print("false")
            if i[2] == "=":
                if int(dict[i[1]]) == int(dict[i[3]]):
                    print("true")
                else:
                    print("false")
            if i[2] == ">":
                if int(dict[i[1]]) > int(dict[i[3]]):
                    print("true")
                else:
                    print("false")
        else:
            print("undefined")
            
        
        
         