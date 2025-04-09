# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        visited=[[False  for i  in range(len(grid[0]))]  for j in range(len(grid))]
        def inbound(r,c):
            return   0<=r<len(grid)  and 0<=c<len(grid[0])
        par=0
        def dfs(visited,row,col):
                nonlocal par
                visited[row][col]=True
                for rc,cc in dir:
                    curr=row+rc
                    curc=col+cc
                    if inbound(curr,curc)   and  grid[curr][curc]:
                        if not visited[curr][curc]:
                          dfs(visited,curr,curc)
                    else:
                          par+=1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                   dfs(visited,r,c)  
                   return par
        return par                