# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        nums.sort()
        for  i in  range(len(nums)):
            if  nums[i]==target:
                arr.append(i)
        return arr
