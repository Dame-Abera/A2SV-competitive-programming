# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        deck=defaultdict(list)
        par=0
        for r in range(len(isConnected)):
            for c in  range(len(isConnected)):
                if isConnected[r][c]==1  and r!=c:
                      deck[r].append(c)
                      deck[c].append(r)
        print(deck)              
        def dfs(node,visited):
                  visited.add(node)
                  
                  if node in deck:
                    for i  in deck[node]:
                        if i not  in visited:
                             dfs(i,visited)
        visited=set()    
        for  i in range(len(isConnected)):
              if i not in visited  :
                par+=1
                dfs(i,visited)
                
        return par        

