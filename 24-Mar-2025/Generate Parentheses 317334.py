# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtrack(path):

            if len(path)==n*2:
                i=0
                for l in range(len(path)-1,-1,-1):
                    print(l)
                    if path[l]==")":
                        i+=1
                    else:
                        i-=1
                    if i<0:
                        break

                else:
                    r="".join(path[:])
                    if r.count("(")==r.count(")")  and r not in ans: 
                       ans.append(r)                
                return 
            path.append("(")             
            backtrack(path)   
            path.pop()
            path.append(")")        
            backtrack(path)
            path.pop()
        backtrack([])
        print(ans)
        return ans