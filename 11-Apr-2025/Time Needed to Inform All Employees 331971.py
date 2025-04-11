# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        deck=defaultdict(list)
        res=0
        signal=None
        for i  in range(len(manager)):
            if manager[i]==-1:
                signal=i
            deck[manager[i]].append(i)
        def dfs(node,c):
            nonlocal res
            for i  in deck[node]:
                dfs(i,c+informTime[i])
            print(c)    
            res=max(c,res)
            print(res)
        dfs(-1,0)
        return res