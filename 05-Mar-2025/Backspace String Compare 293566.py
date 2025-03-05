# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=deque()
        for i  in  s:
            if   i=="#":
                if stack:
                 stack.pop()
            else:
                stack.append(i)    
        tstack=deque()
        for i  in  t:
            if i=="#":
                if tstack:
                 tstack.pop()
            else:
                tstack.append(i)       
        print(tstack,stack)         
        return True  if stack==tstack   else False    