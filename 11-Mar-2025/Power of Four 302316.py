# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n==4 or n==1:
            return True
        if n<4:
            return False    
        n=n/4    
        return self.isPowerOfFour(n)     
        