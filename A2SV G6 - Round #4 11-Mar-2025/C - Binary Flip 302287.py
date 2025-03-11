# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C


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
def solve():
    t=inpi()
    for _  in range(t):
        n=inpi()
        arr1=inp()
        arr2=inp()
        one=0
        z=0
        prefix=[]
        
       
        for i  in arr1:
            if i=="1":
                one+=1
            else:
                z+=1    
            prefix.append(one-z)  
        
        flag=True
        for i  in range(len(arr1)):
            if i==n-1:
                if arr1[i]!=arr2[i]:
                   if prefix[i]!=0:
                       flag=False
            else:
                if (arr1[i]==arr2[i] and arr2[i+1]!=arr1[i+1])  or (arr1[i]!=arr2[i] and arr2[i+1]==arr1[i+1]) :
                             if prefix[i]!=0:
                               flag=False
                      

        if flag:
            print("YES")  
        else:
            print("NO")    
        
# Boilerplate
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    if os.path.exists("input.txt"):  # Debugging with file input
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    solve()