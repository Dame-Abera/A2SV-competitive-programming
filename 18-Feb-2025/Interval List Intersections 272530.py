# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res=[]
        f=0
        r=0
        while f<len(firstList) and r<len(secondList):
            if max(firstList[f][0],secondList[r][0])<=min(firstList[f][1],secondList[r][1]):
                res.append([max(firstList[f][0],secondList[r][0]),min(firstList[f][1],secondList[r][1])])
            if secondList[r][1]>firstList[f][1]:
                f+=1
            else:
                r+=1
        return res             

