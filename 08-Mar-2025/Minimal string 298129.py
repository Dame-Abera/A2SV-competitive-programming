# Problem: Minimal string - https://codeforces.com/contest/797/problem/C

import sys
import os
import math
import itertools
import collections
import heapq
from functools import lru_cache
from bisect import bisect_left, bisect_right
from collections import deque
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
def ispal(strs):
    l,r=0,len(strs)-1
    while  r>=l: 
        if strs[r]!=strs[l]:
            return False
        r-=1
        l+=1
    return True             
def solve():
    strs=inp()
    n=len(strs)
    stack=deque()
    suffix=[" "]*n
    ms=strs[-1]
    res=[]
    for i in range(n-1,-1,-1):
        ms=min(ms,strs[i])
        suffix[i]=ms
    for i in range(n): 
        while stack and stack[-1]<=suffix[i]:
            res.append(stack.pop())
        stack.append(strs[i])    
    while stack:
        res.append(stack.pop())        
    print("".join(res))

# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()
