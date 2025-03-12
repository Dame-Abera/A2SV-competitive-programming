# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack=deque()
        queue=deque()
        numqueue=deque()
        for i in range(len(s)):
            stack.append(s[i])
            
            if stack  and stack[-1]=="]":
                stack.pop()
                while stack and stack[-1]!="[":
                    queue.appendleft(stack.pop())
                stack.pop() 
                  
                while  stack and stack[-1].isdigit():
                      numqueue.appendleft(stack.pop())
                stack.append(("".join(queue))*int("".join(numqueue)))
                queue=deque()
                numqueue=deque()
        return "".join(stack)

                    