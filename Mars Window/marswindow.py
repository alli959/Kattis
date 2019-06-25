import sys
year = int(sys.stdin.readline().strip())

month = 4

dict = {

}

value = 2018

while value <= 10000:
    dict[value] = "yes"
    if month == 12:
        value += 3
        month = 2
    else:
        value += 2
        month += 2




if year in dict:
    print(dict[year])
else:
    print("no")




