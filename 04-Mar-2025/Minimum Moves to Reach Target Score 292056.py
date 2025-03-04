# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        while  target>1:
            if target%2==1  or target==2:
                target-=1
            elif  maxDoubles>0:
                target//=2
                maxDoubles-=1
            else:
                return count+target-1
            count+=1     
        return count             

