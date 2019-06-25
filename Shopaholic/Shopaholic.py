import sys
length = int(sys.stdin.readline().strip())
prices = []

temp = sys.stdin.readline().strip()
lister = temp.split(' ')
for i in lister:
    prices.append(int(i))

prices.sort(reverse = True)

totalprice = 0

i = 2

while i < len(prices):
    totalprice += prices[i]
    i += 3
    
print(totalprice)
        