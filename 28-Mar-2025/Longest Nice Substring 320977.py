# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def divide(s):
          if len(s)<=1:
            return ""
          
          set_s=set(s)   
          for i,v in enumerate(s):
             oppcase=v.swapcase()
             if oppcase not in set_s:
                left=divide(s[:i])
                right=divide(s[i+1:])
                if len(left)>=len(right):
                    return left
                else:
                    return right    
             
          return s  
        return divide(s)   