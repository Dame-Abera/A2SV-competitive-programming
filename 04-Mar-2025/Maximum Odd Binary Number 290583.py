# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count=-1
        strs=["0"]*len(s)
        for i  in s:
            if  i=="1":
                count+=1
        strs[-1]="1"
        for  i  in range(count):
            strs[i]="1"
        return "".join(strs)          