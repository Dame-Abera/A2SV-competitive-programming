# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums=[]
        ans=0
        for i   in range(len(nums1)):
            nums.append(nums1[i]-nums2[i])
       
        def mergesort(nums):
            nonlocal ans
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=mergesort(nums[:mid])
            right=mergesort(nums[mid:])
            
            for i  in right:
                idx=bisect_right(left,i+diff)
                ans+=idx
            return merge(left,right)
        def merge(left,right):
            res=[]
            i=0
            j=0
            while i<len(left) and j<len(right):
                if left[i]>=right[j]:
                    res.append(right[j])
                    j+=1
                else:
                      res.append(left[i])    
                      i+=1
            res.extend(left[i:])  
            res.extend(right[j:])      

            return res
        mergesort(nums)  
        return ans  
