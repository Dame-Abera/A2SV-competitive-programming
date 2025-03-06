# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            res=[0]*len(temperatures)
            stack=deque()
            for i,v  in  enumerate(temperatures):
                while stack and temperatures[stack[-1]]<v:
                    a=stack.pop()
                    res[a]=i-a
                stack.append(i)  
            return res      


                  
                  