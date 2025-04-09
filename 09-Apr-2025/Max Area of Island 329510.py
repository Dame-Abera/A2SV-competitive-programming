# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        par=0
        res=0
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(r,c):
            return   0<=r<len(grid)  and 0<=c<len(grid[0])
        def dfs(visited,r,c):
            nonlocal par
            visited.add((r,c))
            par+=1
            for rc,cc in dir:
                nr=rc+r
                nc=cc+c
                
                if inbound(nr,nc) and grid[nr][nc]:
                    if  (nr,nc)  not in visited:
                       
                        print(par)
                        print(nr,nc)
                        dfs(visited,nr,nc)
                
                        
        visited=set()
        for r  in range(m):
            for c  in range(n):
                if grid[r][c]  and (r,c) not in visited:
                  dfs(visited,r,c)
                  res=max(par,res)
                  par=0
        return res

