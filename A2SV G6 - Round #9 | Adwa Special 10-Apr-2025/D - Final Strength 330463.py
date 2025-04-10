# Problem: D - Final Strength - https://codeforces.com/gym/601269/problem/D

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
    n=inpi()
    iarr=inpl()
    
    
    turns=int(math.log2(len(iarr)))
    
        
    def merge(left,right):  
                    res=[]
                    i=0
                    j=0
                    while i<len(left) and j<len(right):
                        if left[i][0]>=right[j][0]:
                            res.append(right[j])
                            j+=1
                        else:
                                res.append(left[i])    
                                i+=1
                    res.extend(left[i:])  
                    res.extend(right[j:])      

                    return res
    def mergesort(arr): 
                    
                    
                    if len(arr)<=1:
                        return arr
                    mid=len(arr)//2
                    left=mergesort(arr[:mid])
                    right=mergesort(arr[mid:])
                    key1=[a[0]  for a in left]
                    key2=[b[0]  for b in right]
                    for i  in left:
                         i[0]+=bisect_left(key2,i[0]) 
                    for j  in right: 
                           j[0]+=bisect_left(key1,j[0])             
                    return merge(left,right)
                            
    arr=[]        
    for j,val  in enumerate(iarr):
        arr.append([val,j])
       
    a=mergesort(arr)
   
    ans=[0]*len(iarr)
    for i  in a:
           ans[i[1]]=i[0]
    print(*ans)       
def main():
        t=inpi()
        for _  in range(t):    
                solve()
            


# Boilerplate
if __name__ == "__main__":
    # sys.setrecursionlimit(1 << 30)
    # threading.stack_size(1 << 27)

    # main_thread = threading.Thread(target=solve)
    # main_thread.start()
    # main_thread.join()
    main()
    