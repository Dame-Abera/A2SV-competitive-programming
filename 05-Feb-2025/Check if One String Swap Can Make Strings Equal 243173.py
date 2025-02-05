# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count=0
        for i in range(len(s1)):
            if s2[i]!=s1[i]:
                count+=1
        return  count<=2 and sorted(s1)==sorted(s2)
                 