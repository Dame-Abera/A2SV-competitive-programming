# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections    import  defaultdict
n,k=map(int,input().split())
arr=list(map(int,input().split()))
deck=defaultdict(int)
l=0
res=[0,0]
for r in range(len(arr)):
    deck[arr[r]]+=1
    while  l<r and len(deck)>k:
        if deck[arr[l]]==1:
            del deck[arr[l]]
        else:
            deck[arr[l]]-=1
        l+=1    
    if  r-l>res[1]-res[0]:        
      res=[l,r] 
print(res[0]+1,res[1]+1)     
