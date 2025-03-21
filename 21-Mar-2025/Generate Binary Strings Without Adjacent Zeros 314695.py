# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        def backtrack(path):
            if len(path)==n:
                ans.append("".join(path[:]))
                # for i  in range(1,len(path)):
                #     if path[i]=="0" and path[i-1]=="0":

                return 
       
         
            if not path or path[-1]=="1":
                    path.append("0")
                    print(path)
                    backtrack(path)
                    path.pop()
                   
            path.append("1")  
            print(path)
            backtrack(path) 
            path.pop()
        backtrack([])
        return ans