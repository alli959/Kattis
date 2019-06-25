import sys

menuLength = int(sys.stdin.readline().strip())
menuItemsString = sys.stdin.readline().strip()
orderLength = int(sys.stdin.readline().strip())
orderItemsString = sys.stdin.readline().strip()

menuItems = menuItemsString.split(' ')
orderItems = orderItemsString.split(' ')

returnItem = []

def outputs(ready, menuItems, orderItem):

    resault = []

    while orderItem > 0:
            resault.append(int(ready[orderItem])+1)
            orderItem -= int(menuItems[ready[orderItem]])

    resault.sort()
    value = ""
    for i in resault:
        value += str(i) + " "
    return value
    

ready = ["Impossible"]*100000
ready[0] = 0
for i in range(menuLength):
    menuItem = int(menuItems[i])
    for j in range(30000):
        if isinstance(ready[j],int):
            if ready[j] >= 0:
                if ready[j + menuItem] == "Impossible":
                    ready[j+menuItem] = i
                else:
                    ready[j+menuItem] = "Ambiguous"
        
        if ready[j] == "Ambiguous":
            ready[j + menuItem] = "Ambiguous"

for i in orderItems:
    orderItem = int(i)
    if ready[orderItem] == "Impossible":
        print("Impossible")
    elif ready[orderItem] == "Ambiguous":
        print("Ambiguous")
    else:
        print(outputs(ready,menuItems,orderItem))

