# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}
        n=len(nums)
        if n==1:
            return nums[0]
        cache[0]=nums[0]
        cache[1]=max(nums[1],nums[0])
        
        def dp(i):
            if i  in cache:
                return cache[i]
            cache[i]=max(dp(i-1),nums[i]+dp(i-2))
            return cache[i]
        print(cache)    
        return dp(n-1)
        