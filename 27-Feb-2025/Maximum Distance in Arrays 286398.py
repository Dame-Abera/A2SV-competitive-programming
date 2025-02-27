# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        curmin=arrays[0][0]
        curmax=arrays[0][-1]
        res=0

        for i in range(1,len(arrays)):
            res=max(res,arrays[i][-1]-curmin,curmax-arrays[i][0])
            curmax=max(curmax,arrays[i][-1])
            curmin=min(curmin,arrays[i][0])
        return res     