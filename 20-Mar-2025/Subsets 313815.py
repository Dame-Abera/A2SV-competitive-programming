# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(path,start):
             
                
                ans.append( path[:] )

                for i in  range(start,len(nums)):

                     path.append( nums[i] )
                     
                     backtrack( path,i+1 )

                     path.pop()

        backtrack([],0)    

        return  ans