import sys

def checkBoard(board):
    arr = []
    countk = 0
    for i in board:
        temp = list(i)
        arr.append(temp)
    
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'k':
                countk += 1
                if i - 2 >= 0:
                    if j + 1 <= 4:
                        if arr[i-2][j+1] == 'k':
                            return "invalid"
                    if j-1 >= 0:
                        if arr[i-2][j-1] == 'k':
                            return "invalid"
                if i+2 <= 4:
                    if j+1 <= 4:
                        if arr[i+2][j+1] == 'k':
                            return "invalid"
                    if j-1 >= 0:
                        if arr[i+2][j-1] == 'k':
                            return "invalid"
                if j-2 >= 0:
                    if i+1 <= 4:
                        if arr[i+1][j-2] == 'k':
                            return "invalid"
                    if i-1 >= 0:
                        if arr[i-1][j-2] == 'k':
                            return "invalid"
                if j+2 <= 4:
                    if i+1 <= 4:
                        if arr[i+1][j+2] == 'k':
                            return "invalid"
                    if i-1 >= 0:
                        if arr[i-1][j+2] == 'k':
                            return "invalid"
    
    if countk < 9 or countk > 9:
        return "invalid"
    return "valid"
    

arr = []
for i in range(5):
    line = sys.stdin.readline().strip()
    arr.append(line)

print(checkBoard(arr))