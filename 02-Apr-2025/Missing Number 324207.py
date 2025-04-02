# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m=max(nums)
        if m<len(nums):
            return m+1
        return sum(i  for i  in   range(max(nums)+1))-sum(nums)