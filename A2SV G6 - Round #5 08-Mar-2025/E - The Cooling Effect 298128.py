# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

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

def solve():
    
            t = inpi()
            

            for _ in range(t):
                inp()
                n,k =inpl()
                pos =inpl()
                temp = inpl()
                all = [float('inf')] * n  
                for i in range(k):  
                    all[pos[i] - 1] = temp[i]  

                forward = [float('inf')] * n  
                forward[0] = all[0]  
                for i in range(1, n):  
                    forward[i] = min(forward[i - 1] + 1, all[i])  

                backward = [float('inf')] * n  
                backward[-1] = all[-1]  
                for i in range(n - 2, -1, -1):  
                    backward[i] = min(backward[i + 1] + 1, all[i])  

                result = [min(forward[i], backward[i]) for i in range(n)]  
                print(*result) 
# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()
