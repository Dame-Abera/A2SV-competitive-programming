# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        arr=[]
        stack=deque()
        paths=path.split("/")
        print(paths)
        p=[]
        for i  in paths:
              if i:
                p.append(i)
        print(p)        
        for i in p:
            if i!="." and  i!="..":
                stack.append(i)
            else:
                if stack and  i=="..":
                    stack.pop()  
                     
        return "/"+"/".join(stack)          