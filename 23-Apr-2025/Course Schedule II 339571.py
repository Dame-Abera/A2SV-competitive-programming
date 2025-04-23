# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[]   for _  in range(numCourses)]
        incoming=[0 for i  in range(numCourses)]
        q=deque()
        order=[]
        for c,p in prerequisites:
            graph[p].append(c)
            incoming[c]+=1
        for i  in range(len(incoming)):
            if incoming[i]==0:
                q.append(i)
        while q:
            f=q.popleft()
            order.append(f)
            for neigh in graph[f]:
                incoming[neigh]-=1
                if incoming[neigh]==0:
                     q.append(neigh)
        if len(order)!=numCourses:
            return []     
        else:
            return order          