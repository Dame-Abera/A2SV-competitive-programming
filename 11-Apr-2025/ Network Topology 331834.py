# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

import sys
import os
import math
import threading
import itertools
import collections
import heapq
from functools import lru_cache
from bisect import bisect_left, bisect_right
from collections import defaultdict
from collections import Counter
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
b="bus topology"
u= "unknown topology"
r="ring topology"
s="star topology"

def solve():
    n,m=inpl()
    deck=defaultdict(list)
    for i   in range(m):
        a,p=inpl()
        deck[a].append(p)
        deck[p].append(a)
    arr=[]    
    for i  in deck:  
        arr.append(len(deck[i]))
    c=Counter(arr)     
    
    v=c.values()
    if len(c)==2 and c[1]==2 and 2 in c:
        print(b)

    elif len(c)==1 and 2 in c :
        print(r)    
    elif len(c)==2 and  c[max(v)]==1 and c[min(v)]>2:
           print(s)
    else:
        print(u)

# Boilerplate
if __name__ == "__main__":
    # sys.setrecursionlimit(1 << 30)
    # threading.stack_size(1 << 27)

    # main_thread = threading.Thread(target=solve)
    # main_thread.start()
    # main_thread.join()
    solve()
    