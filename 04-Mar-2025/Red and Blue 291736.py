# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B


import sys
import os
import math
import itertools
from collections import Counter
import heapq
from functools import lru_cache
from bisect import bisect_left, bisect_right
from collections import defaultdict
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

def solve():
    t=inpi() 
    for _ in range(t):
        n=inpi()
        r=inpl()
        m=inpi()
        b=inpl()
        maxa=0
        maxb=0
        prefix1=[]
        prefix2=[]
        curr=0
        
        for i in r:
            curr+=i
            maxa=max(curr,maxa)
            prefix1.append(curr)

        curr=0    
        for i in b:
            curr+=i
            maxb=max(maxb,curr)
            prefix2.append(curr)
        print(maxa+maxb)

# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()
