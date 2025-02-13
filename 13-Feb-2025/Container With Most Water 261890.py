# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        area=0
        while  r>=l:
            area=max(area,(r-l)*min(height[l],height[r]))
            if height[r]>=height[l]:
                l+=1
            else:
                r-=1 
        return  area