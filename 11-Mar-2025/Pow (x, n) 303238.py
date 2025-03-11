# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        base=1
        def pov(x,n):
            if n==0:
                return 1
            curr=pov(x,n//2)  
            if n%2==1:
                
                 return  x*curr*curr
            else:     
              return   curr*curr
        if n>=0:
            return pov(x,n)
        else:
            return 1/pov(x,abs(n))         