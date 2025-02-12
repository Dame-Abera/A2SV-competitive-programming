# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        r=len(skill)-1
        l=0
        c=skill[0]+skill[r]
        res=0
        while r>=l:
            if skill[r]+skill[l]==c:
                res+=skill[r]*skill[l]
            else:
                return   -1  
            r-=1
            l+=1    
        return res  

