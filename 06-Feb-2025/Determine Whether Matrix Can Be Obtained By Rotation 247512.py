# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        def transpose(matrix) :
         i,j=0,0
         res=[]
         while i<len(matrix[0]):
            arr=[]
            while j<len(matrix):
                arr.append(matrix[j][i])
                j+=1
            i+=1 
            j=0   
            res.append(arr)  
         return res
        if mat==target:
            return True   
        mat=transpose(mat)
        
        for k in range(n):
            mat[k]=mat[k][::-1]
        print(mat)        
        if mat==target:
                return True 
        mat=transpose(mat)
           
        for a in range(len(mat)):
            mat[a]=mat[a][::-1]  
        print(mat)      
        if mat==target:
                return True            
        mat=transpose(mat)
          
        for n in range(n):
            mat[n]=mat[n][::-1] 
        print(mat)       
        if mat==target:
                return True 
                 
        return False 
                             
        