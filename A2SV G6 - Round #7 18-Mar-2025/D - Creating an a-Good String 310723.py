# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

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
 
def helper(n,arr,a):
    
    if n==1:
             return 0 if arr[0]==a else 1
    mid=n//2 
    nxt=chr(ord(a)+1)
    leftmismatch=sum(1 for i  in range(mid)  if arr[i]!=a)
    rightmismatch=sum(1 for i  in range(mid,n) if arr[i]!=a)
    leftresult=helper(mid,arr[:mid],nxt)+rightmismatch
    rightresult=helper(mid,arr[mid:],nxt)+leftmismatch
    return min(leftresult,rightresult)
def solve():
    t=inpi()
    for _ in range(t):
        n=inpi()
        arr=inp()
        print(helper(n,arr,"a")) 
# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=solve)
    main_thread.start()
    main_thread.join()
    