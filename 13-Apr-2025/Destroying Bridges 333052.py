# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

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
y="YES"
n="NO"
# Output optimization
def printl(arr, sep=" "): 
    sys.stdout.write(sep.join(map(str, arr)) + "\n")

# Constants
INF = float('inf')
MOD = 10**9 + 7


def solve():
    t=inpi()
    for i  in range(t):
        n,k=inpl()
        if k>=n-1:
            print(1)
        else:
            print(n)    


# Boilerplate
if __name__ == "__main__":
    # sys.setrecursionlimit(1 << 30)
    # threading.stack_size(1 << 27)

    # main_thread = threading.Thread(target=solve)
    # main_thread.start()
    # main_thread.join()
    solve()
    