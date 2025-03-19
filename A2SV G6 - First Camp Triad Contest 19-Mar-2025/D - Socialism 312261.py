# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

import sys
import os
import math
import itertools
import collections
import heapq
from functools import lru_cache
from bisect import bisect_left, bisect_right

# Fast input
input = sys.stdin.read
def inp(): return sys.stdin.readline().strip()
def inps(): return sys.stdin.readline().split()
def inpi(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

# Output optimization
def printl(arr, sep=" "): 
    sys.stdout.write(sep.join(map(str, arr)) + "\n")


INF = float('inf')
MOD = 10**9 + 7
             
def solve():
    t=inpi()
    for _  in range(t):
        n,k=inpl()
        arr=inpl()
        arr.sort(reverse=True)
        # l=0
        # r=n-1
        # avg=0
        # sum=0
        # count=0
        # res=0
        # while r>=l:
        #     if avg>=k:
        #         sum+=arr[l]
        #         count+=1
        #         l+=1
        #     else:
        #         sum+=arr[r]   
        #         count+=1
        #         r-=1
        #     avg=sum/count
        #     if avg>=k:
        #         res=max(count,res)
        prefix=[]
        cur=0
        for i in arr:
            cur+=i
            prefix.append(cur)
        j=0    
        while  j<n and prefix[j]/(j+1)>=k:
             j+=1
        print(j)      
   
# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()
