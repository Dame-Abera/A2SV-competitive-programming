# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t=int(input())
for _  in range(t):
    n=int(input())
    
    arr=list(map(int,input().split()))
    l=0
    tot=0
    mex=float("-inf")
    for i in  range(len(arr)):
        if  arr[l]>0 and arr[i]>0:
             mex=max(mex,arr[i])
        elif arr[l]<0 and  arr[i]<0:
            mex=max(mex,arr[i])
        else:
            tot+=mex
            l=i
            mex=arr[i]
        if i==len(arr)-1:
            tot+=mex   
    print(tot)