import sys
howmany = int(sys.stdin.readline().strip())



for i in range(howmany):
    veclen = int(sys.stdin.readline().strip())
    temp1 = sys.stdin.readline().strip()
    temp2 = sys.stdin.readline().strip()
    arr1 = temp1.split(' ')
    arr2 = temp2.split(' ')
    vec1 = []
    vec2 = []
    for j in arr1:
        vec1.append(int(j))
    for j in arr2:
        vec2.append(int(j))
    vec1.sort()
    vec2.sort(reverse = True)

    j = 0
    number = 0
    while j<len(vec1):
        number += (vec1[j] * vec2[j])
        j += 1


    print("Case #" + str(i+1) + ": " + str(number))


