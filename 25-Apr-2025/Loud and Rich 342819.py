# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
            graph=[[] for i  in range(len(quiet))]
            res=[-1]*len(quiet)
            for a,b in richer:
                graph[b].append(a)
            def dfs(node):
                if res[node] != -1:
                  return res[node]
                res[node]=node
                for i  in graph[node]:
                    newnode=dfs(i)
                    if quiet[newnode]<quiet[res[node]]:
                        res[node]=newnode
                newnode=res[node]    
                return res[node]   
            for i  in range(len(quiet)):
                   dfs(i)
            return res        