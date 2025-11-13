# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        count=0
        hash={}
        @lru_cache
        def dp(i):
            if i==n:
                return 1
            print(i)  
            if s[i]=="0":
                return 0
            if i+1<n and int(s[i:i+2])<=26 and int(s[i:i+2])>=10 :
                return dp(i+1)+dp(i+2)
            else:    
                return dp(i+1)
            
        return dp(0) 
             