# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        r=len(people)-1
        l=0
        boat=0
        while r>=l:
            if people[r]+people[l]>limit:
                boat+=1
                r-=1
            else:
                boat+=1
                r-=1
                l+=1    
        return boat         