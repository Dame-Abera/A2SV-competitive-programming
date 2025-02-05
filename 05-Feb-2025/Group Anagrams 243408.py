# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        defdic=defaultdict(list)
        for i in strs:
        
            defdic["".join(sorted(i))].append(i)
           
        ans=list(defdic.values())
        return ans
