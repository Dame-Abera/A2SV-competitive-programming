# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        a1=0
        a2=1
        res=0
        if n==0 or n==1:
            return n
        for i  in range(1,n):
            res=a1+a2
            a1=a2
            a2=res
            print(a1,a2)
        return res

        