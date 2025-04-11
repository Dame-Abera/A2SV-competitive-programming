# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res=[[]  for i  in range(n)]
        deck=defaultdict(list)
        for a,b  in edges:
            deck[b].append(a)
        mem={}
        def dfs(node):

            if node in mem:
                return mem[node]
            v=set()
            if node  in deck:
                
                for i  in deck[node]:
                     v.add(i)
                     v.update(dfs(i))
                     dfs(i)
            mem[node]=v
            return v   
        for i in range(n):
             l=[]
             dfs(i)
             res[i]=sorted(dfs(i))
        return res     
              