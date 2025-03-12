# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        n-=1
        k-=1
        @lru_cache
        def helper(n,k):
            if n==0:     
                return 0   
            
            l=k-(2**(n-1))
            if k<2**(n-1):
    
                return helper(n-1,k)
            else:  
                return 1-helper(n-1,l) 
        return int(helper(n,k))  


