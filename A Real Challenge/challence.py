import sys
import math

number = int(sys.stdin.readline().strip())
sq = math.sqrt(number)
returner = sq + sq + sq + sq
if returner.is_integer():
    print(int(returner))
else:

    print(returner)