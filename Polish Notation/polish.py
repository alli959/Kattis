import sys
import collections
caseNr = 1

def isInt(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False

def operators(op, a, b):
    if op == "+":
        if not isInt(a) or  not isInt(b):
            return "+ " + str(a) + " " + str(b)
        else:
            return str(int(a)+int(b))
    elif op == "-":
        if not isInt(a) or  not isInt(b):
            return "- " + str(a) + " " + str(b)
        else:
            return str(int(a) - int(b))
    else:
        if not isInt(a) or  not isInt(b):
            return "* " + str(a) + " " + str(b)
        else:
            return str(int(a)*int(b))

def checker(lister):
  returner = []

  for i in lister:
    if i == "+" or i == "-" or i == "*":
      b = returner.pop()
      a = returner.pop()
      result = operators(i, b, a)
      returner.append(result)
    else:
      returner.append(i)

  return returner.pop()


for i in range(5):
    returner = []
    testString = sys.stdin.readline().strip()
    if len(testString) == 0:
        break
    lister = testString.split(' ')
    lister.reverse()
    returner = checker(lister)
    stringer = str(returner)
    newlister = stringer.split(' ')
    print("Case " + str(caseNr) + ": " + stringer)
    caseNr += 1
  