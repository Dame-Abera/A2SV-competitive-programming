# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        def inbound(r,c):
            return 0<=r<len(matrix)  and 0<=c<len(matrix[0])
        vis=set()    
        count=1
        res=0
        memo=[[-1 for _ in range(len(matrix[0]))] for j  in range(len(matrix))]
        def dfs(r,c): 
            if memo[r][c]!=-1:
                return memo[r][c]
            count=1
            for rc,cc in dir: 
                nr=rc+r
                nc=cc+c
                print(count)
                if inbound(nr,nc)  and matrix[nr][nc]>matrix[r][c]:         
                    count=max(count,dfs(nr,nc)+1)
            memo[r][c]=count    
            return count
        ans=0    
        for  i  in range(len(matrix)):
            for j  in range(len(matrix[0])): 
                      ans=max(ans,dfs(i,j))
        return ans