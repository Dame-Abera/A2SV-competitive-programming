# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        l=0
        r=(len(queries))-1
        ans=-1

        if max(nums)<=0:
            return 0
        def can(mid):
            temp=[0]*(len(nums)+1)
            num=nums[:]
            
            
            for i  in range(mid+1):
                 temp[queries[i][0]]-=queries[i][2]
                 temp[queries[i][1]+1]+=queries[i][2]
            
            for i  in range(1,len(temp)):
                  temp[i]+=temp[i-1]
              
            for i  in range(len(nums)):
                num[i]+=temp[i]
            
            return max(num)<=0
        while r>=l:
            mid=(l+r)//2
            if can(mid):
                r=mid-1
                ans=mid+1
            else:
                l=mid+1
        return ans
