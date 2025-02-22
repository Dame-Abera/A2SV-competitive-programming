# Problem: Good Subarrays - https://codeforces.com/problemset/problem/1398/C

from collections import defaultdict
t=int(input())
for _ in range(t):
    arr=[]
    n=int(input())
    strs=input()
    for i  in strs:
        arr.append(int(i))
    prefix=[0] 
    
    for j in arr:
        prefix.append(prefix[-1]+j)
    deck=defaultdict(int)  
    res=0
    
    for k in range(len(prefix)):
        if prefix[k]-k in deck:
            res+=deck[prefix[k]-k]
        deck[prefix[k]-k]+=1
    print(res)    
