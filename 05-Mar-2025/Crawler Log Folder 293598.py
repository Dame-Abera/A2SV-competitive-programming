# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=deque()
        for i  in logs:
            if i!="./" and i!="../":
                stack.append(i)
            elif i=="../":
                if stack: 
                 stack.pop()    
        return len(stack)