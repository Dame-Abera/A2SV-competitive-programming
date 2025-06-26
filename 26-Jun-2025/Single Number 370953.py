# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for i in nums:
           result^=i
        return result 

            
        