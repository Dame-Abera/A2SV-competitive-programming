# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B


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
    # class Node:
    #     def __init__(self, value):
    #         self.value = value
    #         self.children = []

    #     def add_child(self, child_node):
    #         self.children.append(child_node)

    # class Tree:
    #     def __init__(self, root_value):
    #         self.root = Node(root_value)

    #     def add_child(self, parent, value):
    #         child = Node(value)
    #         parent.add_child(child)
    #         return child
    
    # head=Node(0)   
    
    # root=Node(1)  
    # root.children=deck[1]
    # del deck[1]
    # for c in root.children:
    #     print(c.value)
    # def traverse():     
    #    for i  in deck:
    #        print(i)
    n=inpi()
    count=2
    deck=defaultdict(list)
    c=0
    def check(arr):
        c=0
        for i  in arr:
            if i in deck:
                c+=1
        return len(arr)-c>=3
        
                
    for i  in range(n-1):
        j=inpi()
        deck[j].append(count)
        count+=1
    for i   in deck:
        
        if not check(deck[i]):
            
            print("No")  

            break
    else:
        print("Yes")    
   

    

# Boilerplate
if __name__ == "__main__":
    # sys.setrecursionlimit(1 << 30)
    # threading.stack_size(1 << 27)

    # main_thread = threading.Thread(target=solve)
    # main_thread.start()
    # main_thread.join()
    solve()
            
