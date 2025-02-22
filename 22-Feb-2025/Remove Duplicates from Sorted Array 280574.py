# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        for right in range(1,len(nums)):
            if nums[left]!=nums[right]:
                nums[left+1],nums[right]=nums[right],nums[left+1]
                left+=1
           
        return left+1
        