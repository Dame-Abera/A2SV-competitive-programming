# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while r>=l:
            mid=(l+r)//2
            
            if matrix[mid][0]<=target  and  target<=matrix[mid][len(matrix[mid])-1]:
                    ls=0
                    rs=len(matrix[mid])-1
                    while rs>=ls:
                        mids=(rs+ls)//2
                        if matrix[mid][mids]==target:
                            return True
                        elif matrix[mid][mids]>target:
                            rs=mids-1
                        else:
                            ls=mids+1 
                    return False          
            elif target>matrix[mid][len(matrix[mid])-1]:
                l=mid+1
            else:
                r=mid-1  
        return False        
