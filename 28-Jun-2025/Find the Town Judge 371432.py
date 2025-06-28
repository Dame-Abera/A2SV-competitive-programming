# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
            deck=defaultdict(set) 
            s=set() 
            if n==1:
                return 1
            for t  in trust:
                     deck[t[1]].add(t[0])
                     s.add(t[0])
            for i  in deck:
                if len(deck[i])==(n-1) and i  not in s:
                    return i
            return -1           