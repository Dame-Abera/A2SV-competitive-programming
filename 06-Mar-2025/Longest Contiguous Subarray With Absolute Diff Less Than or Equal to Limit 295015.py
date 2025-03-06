# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res=0
        inc=deque()
        dec=deque()
        l=0
        for r in range(len(nums)):
            while inc and  inc[-1]<nums[r]:
                inc.pop()
            inc.append(nums[r])   
            while dec and dec[-1]>nums[r]:
                dec.pop()
            dec.append(nums[r]) 
            while inc[0]-dec[0]>limit  :
                left=nums[l]
                if dec[0]==left:
                    dec.popleft()
                
                elif inc[0]==left:
                   inc.popleft()
                l+=1  
            res=max(res,r-l+1)
            
        return res