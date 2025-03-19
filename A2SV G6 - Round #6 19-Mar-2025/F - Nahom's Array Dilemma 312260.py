# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

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
def helper(arr):
    prefix=[0]
    stack=[]
    
    for i  in arr:
             prefix.append(i+prefix[-1])
    for j in range(len(arr)):
            while stack and arr[stack[-1]]<=arr[j]:
                 s=stack.pop()
                 if prefix[j]-prefix[s]>0:
                       return False
                     
            stack.append(j)
    return True        
def solve():
    t=inpi()
    for _ in range(t):
        n=inpl()
        arr=inpl()
        
        rev=arr[::-1]
        if helper(arr)  and helper(rev):
             print("YES")
        else:
             print("NO")

# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=solve)
    main_thread.start()
    main_thread.join()
    