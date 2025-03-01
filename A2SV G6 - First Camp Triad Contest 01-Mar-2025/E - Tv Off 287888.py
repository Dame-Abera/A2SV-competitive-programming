# Problem: E - Tv Off - https://codeforces.com/gym/589822/problem/E

 
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
    n = inpi()
    segments = []
    coord_set = set()
    # Collecting segments and unique coordinates
    for _ in range(n):
        l, r = inpl()
        segments.append((l, r + 1))
        coord_set.add(l)
        coord_set.add(r + 1)

    # Coordinate compression
    coord_list = sorted(coord_set)
    coord_map = {v: i for i, v in enumerate(coord_list)}
    m = len(coord_list)

    # Prefix array to track coverage
    coverage = [0] * (m + 1)
    for l, r in segments:
        coverage[coord_map[l]] += 1
        coverage[coord_map[r]] -= 1

    # Compute prefix sums for coverage
    for i in range(1, m):
        coverage[i] += coverage[i - 1]

    # Compute `pref` array, which stores the count of moments covered exactly once
    pref = [0] * m
    for i in range(1, m):
        pref[i] = pref[i - 1] + (1 if coverage[i - 1] == 1 else 0)

    # Find redundant segment
    for i, (l, r) in enumerate(segments):
        if pref[coord_map[r]] - pref[coord_map[l]] == 0:
            print(i + 1)
            return

    print(-1)
       
# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()


