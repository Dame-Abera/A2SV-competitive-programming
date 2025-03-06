# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=deque()
        res=0
        temp=0
        for i   in s:
            if i=="(":
                stack.append(i)
            else:
                if stack and stack[-1]=="(":
                    stack.pop()
                    if stack and stack[-1]!="(":
                        stack[-1]+=1  
                    else:
                        stack.append(1)     
                else:
                    a=stack.pop()  
                    temp=a*2
                    if stack and stack[-1]=="(":
                        stack.pop()
                        if stack and stack[-1]!="(":
                            stack[-1]+=temp
                        else:     
                           stack.append(temp)
                    elif stack:
                        stack[-1]+=temp
                    else:
                        stack.append(temp)    
            print(stack)     
        print(stack)                 
        return stack[0]
        