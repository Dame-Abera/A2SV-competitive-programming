# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import defaultdict
n=int(input())
l=0
res=0
for i in range(n):
    h=int(input())
    string=input()
    m1=defaultdict(int)
    m2=defaultdict(int)
    res=0
    for j in string:
        m1[j]+=1
    for k in string:
        m2[k]+=1
       
        if m1[k]==1:
            del m1[k]
        else:
            m1[k]-=1
        res=max(res,len(m1)+len(m2))
    print(res)
