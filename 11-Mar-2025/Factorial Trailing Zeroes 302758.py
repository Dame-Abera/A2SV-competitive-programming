# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
          if n==0 or n==1:
            return 1 
          return factorial(n-1)*n
        s=factorial(n)
        count=0  
        while s>=0:
            if s%10!=0:
                return count
            count+=1
            s//=10  
        return count  