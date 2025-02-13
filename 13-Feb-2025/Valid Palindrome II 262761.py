# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        def finisher(l,r):
            while r>l:
                if  s[r]!=s[l]:
                    return False
                r-=1
                l+=1
            return True    
        while  r>=l:
            if  s[l]==s[r]:
               l+=1
               r-=1
            else:
                return finisher(l+1,r) or finisher(l,r-1)
        return  True            