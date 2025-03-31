# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can(mid):
            ct=1
            cursum=0
            res=float("-inf")
            for i in nums:    
                if cursum+i>mid:
                    cursum=i
                    print(cursum)
                    ct+=1
                else:
                    cursum+=i 
                res=max(res,cursum)
            return [ct,res]
        l=max(nums)
        r=sum(nums)
        ans=float("inf")
        while r>=l:
            mid=(r+l)//2
            f=can(mid)
            # if f[0]==k:
            #     ans=min(ans,f[1])

            if f[0]<=k:
                r=mid-1
                ans=min(ans,f[1])
            else:
                l=mid+1
        return ans