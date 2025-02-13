# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        l,res=0,0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            res=max(res,r-l+1)    
            hashset.add(s[r])  
        return res      

