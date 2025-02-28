# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix=[0]
        for i  in nums:
            prefix.append(prefix[-1]+i)
       
        curmin=prefix[0]
        curmax=prefix[0]
        res=0
        for i in prefix:

            res=max(abs(i-curmin),abs(i-curmax),abs(i),res)
            curmin=min(curmin,i)
            curmax=max(curmax,i)
       
        return res 
