# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        k=k%len(nums)
        r=k-1
        l=0
        if  len(nums)==1:
            return  nums
        while r>=l:
            print(l,r)
            nums[r],nums[l]=nums[l],nums[r]
            r-=1
            l+=1
        l=k
        r=len(nums)-1
        while r>=l:
            nums[r],nums[l]=nums[l],nums[r]
            r-=1
            l+=1
        
