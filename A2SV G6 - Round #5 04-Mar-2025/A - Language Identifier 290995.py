# Problem: A - Language Identifier - https://codeforces.com/gym/591928/problem/A


import sys
import os
import math
import itertools
from collections import Counter
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


INF = float('inf')
MOD = 10**9 + 7

def solve():
   t=inpi()
   for  _   in range(t):
        strs=inp()
        if strs[-2:]=="po":
           print("FILIPINO")
         
        elif strs[-4:]=="desu" or strs[-4:]=="masu":   
            print("JAPANESE") 
        elif strs[-5:]=="mnida":
            print('KOREAN')
         
       

# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()
