# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res=0
        deck=defaultdict(list)
        for i  in employees:
            deck[i.id]=[i.importance,i.subordinates]
        print(deck)    
        def dfs(id):
            nonlocal res
            print(id)
            res+=deck[id][0]
            for i  in deck[id][1]:
                  dfs(i)
        dfs(id)
        return res