# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def __init__(self):
        self.l=False
    def punishmentNumber(self, n: int) -> int:
        def dfs(start,path,strs):
          
            if len("".join(map(str,path)))==len(strs)  and sum(path)==int(sqrt(int(strs))):
                self.l=True
                return 
              
            num=0    
            for i  in range(start,len(strs)):
                num=num*10+int(strs[i])   
                if sum(path)>sqrt(int(strs)):
                    continue
                path.append(num)
                
                dfs(i+1,path,strs)
                path.pop()
            

        res=0
        for i  in range(1,n+1):
            
            self.l=False
            dfs(0,[],str(i*i))
            if self.l:


                   res+=i*i
        return res
                   