# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        def possible(mid):
            ship=1
            cursum=0
            for  w in weights:
                
                
                if cursum+w>mid:
                    cursum=0
                    ship+=1 
                cursum+=w         
            return days>=ship  
        res=sum(weights)       
        while r>=l:
            mid=(r+l)//2
            print(mid)
            if possible(mid):
                
                res=min(res,mid)
                r=mid-1
                print(res)
            else:
                l=mid+1
        return res
      
