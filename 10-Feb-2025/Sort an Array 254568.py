# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mas=max(nums)
        mis=abs(min(nums))
        arr=[0]*(mis+mas+1)
        for i,v in enumerate(nums):
           arr[v+mis]+=1
        index=0
        for idx,val in enumerate(arr):
            for value in range(val):
                nums[index]=idx-mis
                index+=1
        return nums
