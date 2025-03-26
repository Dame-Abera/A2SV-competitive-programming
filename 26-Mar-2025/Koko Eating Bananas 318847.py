# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(mid):
            cap=0
            for p   in piles:
                cap+=ceil(p/mid)
            return cap<=h
        l=1
        r=max(piles)
        ans=None
        while r>=l:
            mid=(r+l)//2
            if can(mid):
                ans=mid
                r=mid-1
                
            else:
                l=mid+1
        return l