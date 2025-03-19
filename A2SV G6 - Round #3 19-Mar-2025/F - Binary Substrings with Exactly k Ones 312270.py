# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import defaultdict
k=int(input())
arr=input()
deck=defaultdict(int)
prefix=[0]
for i in range(len(arr)):
   
    prefix.append(prefix[-1]+int(arr[i]))  
 
ans=0 
for i  in prefix:
    if i-k  in deck:
        ans+=deck[i-k]
    deck[i]+=1
print(ans)

