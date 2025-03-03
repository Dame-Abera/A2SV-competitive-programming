# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count=2
        i=len(nums)-1
        if nums[0]==0 and len(nums)>1:
            return False
        while i>0:
            if nums[i]==0 and i!=len(nums)-1:
                j=i-1
                while j>0 and  count>nums[j]: 
                        count+=1
                        j-=1
                if count>nums[j]:
                    
                    return False
                i=j
                count=2
            
            i-=1
        return True


                 



              