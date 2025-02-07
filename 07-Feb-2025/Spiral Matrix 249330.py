# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
       rows , cols = len(matrix) , len(matrix[0])
       res=matrix[0]
       currow=0
       curcol=len(matrix[0])-1
       rem=len(matrix)*len(matrix[0])-len(matrix[0])
       vert = len(matrix) -1
       hort =len(matrix[0])-1
       hflag = False
       vflag = False
       while rem:
            for _ in range(vert):
                if vflag==False:
                  currow+=1
                else:
                    currow-=1
                res.append(matrix[currow][curcol])  
                rem-=1
            vert-=1
            vflag=True if vflag==False   else False    
            for _ in range(hort):
                if hflag==False:
                  curcol-=1
                else:
                    curcol+=1
                res.append(matrix[currow][curcol]) 
                rem-=1
            hort-=1       
            hflag=True if hflag==False   else False 
                    
       return res    