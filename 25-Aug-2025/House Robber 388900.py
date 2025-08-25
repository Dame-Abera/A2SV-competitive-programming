# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def  dp(i):
            if i==0:
                return nums[0]
            if i==1:
                  return max(nums[1],nums[0])
            if i not in memo:
                print(dp(i-1))
                memo[i]=max(dp(i-2)+nums[i],dp(i-1)) 
            return memo[i]
        memo={}    
        return dp(len(nums)-1)    