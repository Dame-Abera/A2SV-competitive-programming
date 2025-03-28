# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        def getclosest(cur):
            l=0
            r=len(heaters)-1
            ans=float(inf)
            while r>=l:
                mid=(r+l)//2
                print(heaters[mid],cur)
                if cur<heaters[mid]:
                    r=mid-1
                    ans=min(ans,abs(heaters[mid]-cur))
                elif cur>heaters[mid]:   
                    l=mid+1
                    ans=min(ans,abs(heaters[mid]-cur))
                else:
                    return 0
 
            return  ans
            
        res=0
        for i  in houses:
            f=getclosest(i)
            print(f)
            res=max(res,f)
        return res    
