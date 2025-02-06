# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
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
