import sys


#SOURCE:
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/?fbclid=IwAR2NNphI9aYc0dn3vLFmPKGAT4dzu-J6z1dvoinb5YlfUQ3k1Ow46YEYjZs


def KMPSearch(pat, txt): 
    arr = []
    M = len(pat) 
    N = len(txt) 
  
    lps = [0]*M 
    j = 0 
  
    computeLPSArray(pat, M, lps) 
  
    i = 0 
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            arr.append(str(i-j))

            j = lps[j-1] 
  
        
        elif i < N and pat[j] != txt[i]: 
            
            
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    return arr
  
def computeLPSArray(pat, M, lps): 
    length = 0 
    lps[0] 
    i = 1
    while i < M: 
        if pat[i]== pat[length]: 
            length += 1
            lps[i] = length
            i += 1
        else: 
            
            
            
            if length != 0: 
                length = lps[length-1] 
  
                
            else: 
                lps[i] = 0
                i += 1
  

pattern = sys.stdin.readline().strip()

while pattern != "":
    value = sys.stdin.readline().strip()
    arr = KMPSearch(pattern, value)
    string = ' '.join(arr)
    print(string)
    pattern = sys.stdin.readline().strip()


