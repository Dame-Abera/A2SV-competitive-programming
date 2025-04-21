# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        def inbound(a,b):
            return 0<=a<len(grid) and 0<=b<len(grid[0])
        v=set() 
        q=deque() 
        for i  in range(len(grid)):
            for j  in range(len(grid[0])):
                if grid[i][j]==1:
                        v.add((i,j))
                if grid[i][j]==2:
                    q.append((i,j))
        count=0
        if not v:
            return 0
        while q:
            for   i in range(len(q)):
                r,c=q.popleft()
                for rc,cc  in dir:
                    nr=r+rc
                    nc=c+cc       
                    if inbound(nr,nc) and grid[nr][nc]==1 and (nr,nc) in v:
                            v.remove((nr,nc))
                            q.append((nr,nc))
            count+=1
        if v: return -1
        else: return count-1                  