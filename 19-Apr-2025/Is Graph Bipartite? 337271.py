# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color=[0]*len(graph)
        def bfs(node):
            if color[node]:
                return True
            q=deque([node])    
            color[node]=1
            while q:
                print(q)
                
                a=q.popleft()  
                for t   in graph[a]:
                    if color[t]:
                        if  color[t]==color[a]:
                           return False
                    else:
                        color[t]=-1*color[a]
                        q.append(t)
            return True           
        for i  in range(len(graph)):
            if not bfs(i):
                return False
        return True                  