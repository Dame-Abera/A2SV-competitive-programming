# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count=0
        l=0
        
        
        e=-1
        s=-1
        for  i   in range(len(nums)):
            if nums[i]>maxK or nums[i]<minK:
                l=i+1
    
                e=-1
                s=-1
            if nums[i]==minK:
                s=i
        
            if nums[i]==maxK:
               e=i
               
            if e!=-1 and s!=-1:
                print(nums[i],nums[l])
                count+=max(min(s,e)-l+1,0)   
                print(count)
        return count      


