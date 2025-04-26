# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=[[] for i  in range(numCourses)]
        res=[set() for i  in range(numCourses)]
        for p,c in prerequisites:
            graph[c].append(p)
        q=deque()

        def bfs(node,vis):
            q.append(node)
            while q:
                x=q.popleft()
                for i  in graph[x]:
                    if i not in vis:
                        q.append(i)  
                        res[node].add(i)
                        vis.add(i)


            
        for i  in range(len(res)):
            bfs(i,set())
        ans=[]  
        for q in queries:
             ans.append(q[0] in res[q[1]])
        return ans     