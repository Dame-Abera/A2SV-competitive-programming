# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        a=copy.deepcopy(isWater)
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        q=deque() 
        res=[[0 for i  in range(len(isWater[0]))] for j  in range(len(isWater))]
        def inbound(a,b):
            return 0<=a<len(isWater) and 0<=b<len(isWater[0])
        count=0 
        v=set()
        for i in range(len(isWater)):
            for j  in range(len(isWater[0])):
                   if isWater[i][j]==1:
                        q.append((i,j))
                        v.add((i,j))
                        
        while q:
            count+=1
            for i  in range(len(q)):
                   r,c=q.popleft()
                   for rc,cc in dir:
                        nr,nc=r+rc,c+cc  
                        if inbound(nr,nc) and (nr,nc) not in v:
                                    q.append((nr,nc))
                                    res[nr][nc]=count
                                    v.add((nr,nc))

        return res                             