# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

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
    n,k=inpl()
    arr=inpl()
    res=arr[-1]-arr[0]
    ares=[]
    for i in range(len(arr)-1):
       ares.append(arr[i]-arr[i+1])
    ares.sort()   
    print(res+sum(ares[:k-1]))
# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()
   