# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most=max(candies)
        array=[]
        for i in candies:
            if i+extraCandies>=most:
                array.append(True)
            else:
                array.append(False)    
        return array        
