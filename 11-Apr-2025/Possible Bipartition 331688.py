# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        deck=defaultdict(list)
        par=0
        color=[-1]*(n+1)
        flag=True
        for a,b in dislikes:
              deck[b].append(a)
              deck[a].append(b)
              
        def dfs(node):
            nonlocal flag
            if node in deck:
               
                for k  in deck[node]:  
                    
                    if color[k]==-1:
                        color[k]=1-color[node]
                        dfs(k)
                       
                        
                    elif color[k]==color[node]:
                          flag=False
                          break
                                  
         
        for i  in range(1,n+1):
                if color[i]==-1: 
                  color[i]=0
                  dfs(i)
        return flag      