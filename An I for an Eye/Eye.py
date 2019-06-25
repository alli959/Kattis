import math
import sys
wordDict = {
    "at": "@",
    "and": "&",
    "one": "1",
    "won": "1",
    "too": "2",
    "to": "2",
    "two": "2",
    "for": "4",
    "four": "4",
    "bea": "b",
    "bee": "b",
    "be": "b",
    "sea": "c",
    "see": "c",
    "eye": "i",
    "oh": "o",
    "owe": "o",
    "are": "r",
    "you": "u",
    "why": "y",
}





def fixer(stri):
    strin = stri.lower()

    i = 0
    returnstr = ""
    isBreak = False
    changeValue = ""
    changeStart = -1
    changeEnd = -1
    
    while i < len(strin):
        value = ""
        for key, value in wordDict.items():
            if len(strin[i:]) >= len(key):
                if strin[i:i+len(key)] == key:
                    returnstr += value
                    changeValue = value
                    changeStart = i
                    changeEnd = i+len(key)
                    isBreak = True
                    break
        if isBreak:
            newstr = strin[:changeStart] + changeValue + strin[changeEnd:]
            strin = newstr
            changeStart = -1
            changeEnd = -1
            changeValue = ""
            i += 1
            isBreak = False
        else:
            returnstr += strin[i]
            i += 1

    returnstr = returnstr.capitalize()
    return returnstr

length = sys.stdin.readline().strip()
for i in range(int(length)):
    line = sys.stdin.readline().strip()
    print(fixer(line))


