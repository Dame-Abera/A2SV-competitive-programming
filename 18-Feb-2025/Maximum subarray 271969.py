# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixsum=[0]
        
        sums=0
        
        for i  in range(len(nums)):
            prefixsum.append(prefixsum[-1]+nums[i])
        prefixsum=prefixsum[1:] 
        ans=float("-inf")
        minone=float("inf")   
        for cur in prefixsum :
              
              ans=max(ans,cur,cur-minone)
              minone=min(cur,minone)
          
        return ans        
        

        