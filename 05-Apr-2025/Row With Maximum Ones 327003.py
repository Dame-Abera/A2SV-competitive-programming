# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count=0
        res=[0,0]
        for idx,i  in  enumerate(mat):
            if i.count(1)>count:
                  count=i.count(1)
                  res=[idx,i.count(1)]
        return res