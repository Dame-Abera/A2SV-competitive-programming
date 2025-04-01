# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

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
    count=0
    def masha(arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        l=masha(left)
        r=masha(right)
        return merge(l,r)
    def merge(l,r):
        nonlocal count
        if l[0]<=r[0]:
            return l+r
        else:
            count+=1
            return r+l

    n=inpi()
    arr=inpl()
    res=masha(arr)
    if res==sorted(arr):
        print(count)
    else:
        print(-1)   

def main():
    t=inpi()  
    for _ in range(t):
        solve()
        
# Boilerplate
if __name__ == "__main__":
    # sys.setrecursionlimit(1 << 30)
    # threading.stack_size(1 << 27)

    # main_thread = threading.Thread(target=solve)
    # main_thread.start()
    # main_thread.join()
    main()
    
