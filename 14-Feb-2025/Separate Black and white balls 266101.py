# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        arr=list(s)
        count=0
        zcount=s.count("0")
        for  i in range(len(arr)):
            if arr[i]=="1":
                count+=zcount
            else:
              zcount-=1
        return count            