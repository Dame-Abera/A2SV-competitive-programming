# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B


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
    n=inpi() 
    arr=inpl() 
    line=inpi()
    sarr=sorted(arr)
    prefix=[0]
    prefix2=[0]
    curr=0
    for i  in arr:
        curr+=i
        prefix.append(curr)
    curr=0    
    for i    in sarr:
        curr+=i
        prefix2.append(curr)
    
    for i  in range(line):
        t,l,r=inpl()
        if t==1:
            print(prefix[r]-prefix[l-1])
        else:
            print(prefix2[r]-prefix2[l-1])    
# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()