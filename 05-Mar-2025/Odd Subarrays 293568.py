# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

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

# Constants
INF = float('inf')
MOD = 10**9 + 7


def solve():
   t=inpi() 
   for _ in range(t):
       n=inpl()
       arr=inpl()
       curmax=arr[0]
       count=0
       for i  in range(1,len(arr)):
           
            if arr[i]<curmax:
               
                count+=1
                if i<len(arr)-1:
                 curmax=arr[i+1]
            else:
                curmax=max(curmax,arr[i])
       print(count)  
# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()
   