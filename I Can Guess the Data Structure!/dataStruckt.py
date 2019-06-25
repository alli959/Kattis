import sys
import collections
import bisect


isStack = True
isQueue = True
isPrio = True

impossible = False

stack = collections.deque()
queue = collections.deque()
prio = collections.deque()





def stackAdd(value):
    stack.append(value)

def stackRemove():
    if len(stack) == 0:
        return "error"
    else:
        return stack.pop()

def queueAdd(value):
    queue.append(value)

def queueRemove():
    if len(queue) == 0:
        return "error"
    else:
        return queue.popleft()

def prioAdd(value):
    bisect.insort(prio, value)

def prioRemove():
    if len(prio) == 0:
        return "error"
    else:
        return prio.pop()

for i in range(10000):
    strlength = sys.stdin.readline().strip()
    while len(strlength.split(' ')) != 1:
        strlength = sys.stdin.readline().strip()
    if strlength == "":
        break
    length = int(strlength)
    for j in range(length):
        string = sys.stdin.readline().strip()
        lister = string.split(' ')
        
        if isStack:
            if int(lister[0]) == 1:
                stackAdd(int(lister[1]))
            else:
                value = stackRemove()
                if value == "error":
                    impossible = True
                    break
                if value != int(lister[1]):
                    isStack = False
        if isQueue:
            if int(lister[0]) == 1:
                queueAdd(int(lister[1]))
            else:
                value = queueRemove()
                if value == "error":
                    impossible = True

                    break
                if value != int(lister[1]):
                    isQueue = False
        if isPrio:
            if int(lister[0]) == 1:
                prioAdd(int(lister[1]))
            else:
                value = prioRemove()
                if value == "error":
                    print("hello")
                    impossible = True
                    break
                if value != int(lister[1]):
                    isPrio = False

        if isPrio == False and isStack == False and isQueue == False:
            impossible = True
            break

    if impossible:
        print("impossible")
    else:
        arr = []
        if isStack == True:
            arr.append("stack")
        if isQueue == True:
            arr.append("queue")
        if isPrio == True:
            arr.append("priority queue")
        if len(arr) > 1:
            print("not sure")
        else:
            print(arr[0])

    isStack = True
    isQueue = True
    isPrio = True
    impossible = False

    inp = 0
    stack = collections.deque()
    queue = collections.deque()
    prio = collections.deque()

    

    


            



