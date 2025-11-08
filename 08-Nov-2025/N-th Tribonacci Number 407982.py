# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        cache={}
        def Calculatetribonacci(t):
            if t==1:
                return 1
            if t==0:
                return 0
            if t==2:
                return 1    
            if t in cache:
                return cache[t]    
            intermediate_res=Calculatetribonacci(t-1) + Calculatetribonacci(t-2) + Calculatetribonacci(t-3)
            cache[t]=intermediate_res
            return intermediate_res
        return Calculatetribonacci(n)