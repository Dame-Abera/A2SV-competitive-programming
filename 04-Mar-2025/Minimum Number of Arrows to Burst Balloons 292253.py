# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
       
        res=1
        points.sort(key=lambda  a:a[0])
        l=points[0][0]
        r=points[0][1]
        for i  in range(1,len(points)):
            if points[i][0]>r:
                r=points[i][1] 
                
                res+=1
            r=min(r,points[i][1])    
        return res        