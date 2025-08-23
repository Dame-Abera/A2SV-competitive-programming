# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        fn=0
        fn1=1
        memo={}
        def fi(a):
            nonlocal memo
            if a==0 or a==1:
                return a
            print(a)        
            if a not in memo:
                memo[a]=fi(a-1)+fi(a-2)
            

            return memo[a]  

        return fi(n)
        
        

        