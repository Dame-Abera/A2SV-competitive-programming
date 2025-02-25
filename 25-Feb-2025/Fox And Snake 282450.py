# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A


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


INF = float('inf')
MOD = 10**9 + 7
def isval(arr,m,n):
        res=[]    
        for col in range(m):
            for row in range(n):
                if row==0 :
                    continue
                else:
                    if arr[row][col]!=n*(col)+row:
                        return False
        return True     

def solve():
        n,m=inpl()
        flag=True
        for i  in range(n):
            if i%2==0:
                print("#"*m)
            else:
                if flag:
                    print("."*(m-1)+"#")
                else:
                    print("#"+"."*(m-1)) 
                flag=not flag       

# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()