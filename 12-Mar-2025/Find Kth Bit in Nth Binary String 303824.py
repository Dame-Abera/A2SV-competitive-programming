# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        @lru_cache()
        def helper(n):   
            if  n==1:
                return "0"
            s=helper(n-1)
            a=""
        
            for  i  in range(len(s)-1,-1,-1):
                if s[i]=="1":
                    a+='0'
                else:
                    a+="1"    
            return s + "1"+a
        res=helper(n)    
        return     res[k-1]