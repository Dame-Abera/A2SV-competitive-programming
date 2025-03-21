# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def __init__(self):
        self.res="inf"
    def smallestNumber(self, pattern: str) -> str:
        res=1
        def backtrack(path):
            
            if len(path)==len(pattern)+1:
                
                for i  in range(1,len(pattern)+1):
                    if pattern[i-1]=="D" and path[i]>path[i-1]:
                            
                            return
                    elif pattern[i-1]=="I" and path[i]<path[i-1]:
                       
                        return 
               
                self.res=min(self.res,"".join(map(str,path)))
            for  i  in range(1,len(pattern)+2):
               
                if i  not in path:
                    path.append(i)  
                    if len(path)>=2:
                         l=len(path)
                         print(l)
                         if pattern[l-2]=="D" and path[-1]>path[-2]:
                            path.pop()
                            continue
                         elif pattern[l-2]=="I" and path[-1]<path[-2]:
                             path.pop()
                             continue
                    backtrack(path)
                    path.pop()
        backtrack([])
        print(self.res)
        return self.res