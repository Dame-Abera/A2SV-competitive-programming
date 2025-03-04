# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C


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
   
        n,t,c=inpl()
        p=inpl() 
        count=0
        l=0
        for i  in range(n):
             if   p[i]>t:
                  l=i+1
                  
             if  i-l+1==c:
                  count+=1
                  l+=1
                
        print(count)
                       
                  

       
# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()
