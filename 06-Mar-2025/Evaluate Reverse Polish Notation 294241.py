# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=deque()
        arr=["+","-","*","/"]
        
        for i  in tokens:
            if i in arr:
                f=stack.pop()
                s=stack.pop()
                if i=="+":
                  stack.append(f+s)  
                elif i=="/":
                    res=s/f
            
                    if res>0:

                      stack.append(s//f) 
                    else:
                        if res-(s//f):
                           stack.append((s//f)+1)  
                        else:
                            stack.append(s//f)
                elif i=="*":
                    stack.append(f*s) 
                else:
                    stack.append(s-f)    
            else:
                stack.append(int(i))
              
        return stack[0]

             