# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(set)
        if n==1:
            return [0]
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        while len(graph)>2:
            res=[]
            for i  in graph:
                if len(graph[i])==1:
                    res.append(i)
            
            for j in res:
                a=graph.pop(j)
                graph[list(a)[0]].remove(j)
        ans=[]        
        for i  in graph:
            ans.append(i)
        return ans      
                               


                      