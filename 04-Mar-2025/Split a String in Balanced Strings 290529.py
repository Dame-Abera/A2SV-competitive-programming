# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rcount=0
        lcount=0
        res=0
        for i in s:
            if i=="R":
                rcount+=1
            else:
                lcount+=1

            if rcount==lcount:
                res+=1
                rcount=0
                lcount=0
        return res        