# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zcount=0
        l=0
        res=0
        for i  in range(len(nums)):
            if nums[i]==0:
                zcount+=1
            while zcount>k:
                    if nums[l]==0:
                         zcount-=1
                    l+=1   
            res=max(res,i-l+1) 
        return res              

