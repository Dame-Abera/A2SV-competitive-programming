# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r=int(sqrt(c))
        l=0
        while r>=l:
            wep=l**2+r**2
            if wep==c:
                return True
            elif wep>c:
                r-=1
            else:
                l+=1
        return False             