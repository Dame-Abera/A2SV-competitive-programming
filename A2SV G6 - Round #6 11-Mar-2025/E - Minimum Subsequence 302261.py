# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    b = input()
    
    stack = deque()
    count = 0
    res = []
    z=[]
    one=[]
    c=0
    for i  in b:
        
        if i=="0":
            if one:
                now=one.pop()
                z.append(now)
                res.append(now)

                
            else:
                c+=1
                z.append(c)  
                res.append(c)
                  
        else:  
            if z:
                 now=z.pop()
                 one.append(now)
                 res.append(now)
                
            else:
                c+=1
                one.append(c)
                res.append(c)
    print(c)       
    print(*res) 
    