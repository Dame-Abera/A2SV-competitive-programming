# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        l=0
        r=len(nums)-1
        while r>l:
            mid=(l+r)//2
            print(mid)
    
            if nums[mid]>nums[r] :
                l=mid+1
            else:
                r=mid
            
        return nums[l]        
