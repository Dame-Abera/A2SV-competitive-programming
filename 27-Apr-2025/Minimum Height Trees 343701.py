# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        if n==1:
            return [0]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        leaf=deque()    
        e={}
        for i  in graph:
            if len(graph[i])==1:
                leaf.append(i)
            e[i]=len(graph[i])  
                  
        while leaf:
            print(leaf)
            if n<=2:
                return list(leaf)
            for i  in range(len(leaf)):
                a=leaf.popleft()
                n-=1
                for nei in graph[a]:
                    e[nei]-=1
                    if e[nei]==1:
                        leaf.append(nei)

                
          
                               


                      