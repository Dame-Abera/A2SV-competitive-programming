# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

import sys
import os
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right


def inp(): return sys.stdin.readline().strip()
def inps(): return sys.stdin.readline().split()
def inpi(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def printl(arr, sep=" "):
    sys.stdout.write(sep.join(map(str, arr)) + "\n")
    sys.stdout.flush()

INF = float('inf')
MOD = 10**9 + 7

def solve():
    n,k=inpl()
    arr=inpl()
    inc=deque()
    dec=deque()
    count=0
    l=0
    for i in range(len(arr)):
        while inc and arr[inc[-1]]>arr[i]:
               inc.pop()
        inc.append(i)
        while dec and arr[dec[-1]]<arr[i]:
             dec.pop()
        dec.append(i)  
        while arr[dec[0]]-arr[inc[0]]>k:
             l+=1
             if dec[0]<l:
                  dec.popleft()
             if inc[0]<l:
                  inc.popleft()  
        count+=i-l+1          
    print(count) 


if __name__ == "__main__":
    
    if os.getenv("LOCAL"):  
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")

    sys.setrecursionlimit(10**5)  
    solve()

   

 
