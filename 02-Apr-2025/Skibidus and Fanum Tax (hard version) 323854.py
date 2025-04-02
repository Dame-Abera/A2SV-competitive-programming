# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

import sys
import os
import math
import threading
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

# Constants
INF = float('inf')
MOD = 10**9 + 7


def solve():
    t=inpi()
    def getgood(prev,cur,b):
        r=len(b)-1
        l=0
        ans=INF
        while r>=l :
            mid=(l+r)//2   
            if b[mid]-cur>=prev:
                ans=b[mid]-cur
                r=mid-1
            else:
                l=mid+1
            
        return  ans  if ans!=INF else INF 
    for _  in  range(t):
        n,m=inpl()
        a=inpl()
        b=inpl()
        b.sort()
        
        
        for i in range(len(a)):
            if i==0:
                a[i]=min(a[i],b[0]-a[i])
            else:
               f=getgood(a[i-1],a[i],b)
               if f!=INF:
                   if min(f,a[i])>=a[i-1]:
                      a[i]=min(f,a[i])
                   else:
                       a[i]=max(f,a[i])
        
        if all(a[i] >= a[i-1] for i in range(1, n)): 
               print("YES")    
        else:
            print("NO")    
           
# Boilerplate
if __name__ == "__main__":
    # sys.setrecursionlimit(1 << 30)
    # threading.stack_size(1 << 27)

    # main_thread = threading.Thread(target=solve)
    # main_thread.start()
    # main_thread.join()
    solve()
