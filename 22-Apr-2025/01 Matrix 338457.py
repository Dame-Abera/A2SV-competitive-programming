# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res=[[-1 for i  in range(len(mat[0]))] for j  in range(len(mat))]
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        q=deque() 
        for i   in range(len(mat)):
            for j   in range(len(mat[0])):
                    if mat[i][j]==0:
                        res[i][j]=0
                        q.append((i,j))
        def inbound(a,b):
            return 0<=a<len(mat) and 0<=b<len(mat[0])
        
        
        count=0 
        while q:
            count+=1
            print(q)
            for i  in range(len(q)):
                r,c=q.popleft()
                for rc,cc in dir:
                    nr,nc=rc+r,cc+c
                    if inbound(nr,nc):
                        if res[nr][nc]==-1:
                            res[nr][nc]=count
                            q.append((nr,nc))
                        
        return res