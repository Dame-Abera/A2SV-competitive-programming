# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort(reverse=True)
        r=max(candies)
        l=1
        def validate(mid):
            count=0
            ptr=0
            while ptr<len(candies) and candies[ptr]>=mid:
                
                count+=floor(candies[ptr]/mid)
                ptr+=1
            return count>=k
        ans=0    
        while r>=l:
            mid=(l+r)//2
            print(mid)
            if validate(mid):
                l=mid+1
                ans=mid
            else:
                r=mid-1
        return ans            
