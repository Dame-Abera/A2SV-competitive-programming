# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        w,g,b=0,1,2
        deck=defaultdict(list)
    
        color=[0]*numCourses
        for i,v  in prerequisites:
                deck[v].append(i)
        print(deck)        
        def dfs(node): 
            nonlocal w
            nonlocal b
            nonlocal g
            if color[node]==g:
                return False 

            color[node]=g
            # nonlo cal deck
            
            res=True
            for neigh in deck[node]:
                if color[neigh]==0:
                    res=res and  dfs(neigh)
                elif color[neigh]==g:
                    res=res and  dfs(neigh)
            
            color[node]=b
            return res 
        ans=True
        for i  in range(numCourses):
            if color[i]==b:
                continue
            ans = ans and dfs(i)    
        return ans           