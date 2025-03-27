# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left=1
        right=position[-1]-position[0]
        def validate(mid):
            l=0
            r=1
            count=0
            while l<=len(position)-1:
                while r<=len(position)-1 and  position[r]-position[l]<mid:
                      r+=1
              
                l=r
                r=l+1
                count+=1
             
            return count>=m     
        ans=1
        while right>=left:
            mid=(right+left)//2
           
            if validate(mid):
                left=mid+1
                ans=mid
            else:
                right=mid-1    
        return ans