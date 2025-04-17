# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        def inbound(r,c):
            return 0<=r<len(image)  and 0<=c<len(image[0])
        def dfs(visited,r,c):
            visited.add((r,c))
            for rc,cc in dir:
                nr=rc+r
                nc=cc+c
                if inbound(nr,nc) and (nr,nc) not in visited and image[nr][nc]==image[sr][sc]:
                   dfs(visited,nr,nc)
        visited=set()       
        dfs(visited,sr,sc)
        print(visited)
        for a,b in visited:
            image[a][b]=color
        return image    

