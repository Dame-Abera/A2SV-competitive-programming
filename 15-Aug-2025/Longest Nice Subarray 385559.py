# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        used_bits = 0
        res = 0

        for right in range(len(nums)):
           
            while used_bits & nums[right]:
                used_bits ^= nums[left] 
                left += 1

            used_bits |= nums[right]

           
            res = max(res, right - left + 1)

        return res
 