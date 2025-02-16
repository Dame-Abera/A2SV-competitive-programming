# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cur,tot=0,0
        cur=sum(cardPoints[0:k])
        cur1=cur
        j=-1
        for i in range(k-1,-1,-1):
           cur+=cardPoints[j]-cardPoints[i]
           j-=1
           tot=max(tot,cur,cur1)
        return tot