# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        deck=defaultdict(list)
        par=0 
        for a,b  in edges: 
            deck[a].append(b)
            deck[b].append(a)
        def dfs(node,visited,vg):
            visited.add(node)
            vg.add(node)
            for i in deck[node]:
                if i not in visited:
                   dfs(i,visited,vg)
        vg=set()    
        for  i in range(n):
            visited=set()
            if i not in vg:
                dfs(i,visited,vg)
                a=len(visited)
                print(visited,vg)       
                for k in visited:
                    if len(deck[k])!=a-1:
                        break
                else:
                    par+=1        
        return par 