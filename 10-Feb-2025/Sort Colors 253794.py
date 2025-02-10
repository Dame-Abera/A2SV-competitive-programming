# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mas=max(nums)
        arr=[0]*(max(nums)+1)
        for  i,v in enumerate(nums):
            arr[v]+=1
        index=0
        for idx,val in enumerate(arr):
            for value in range(val):
                nums[index]=idx
                index+=1
        return  nums   
