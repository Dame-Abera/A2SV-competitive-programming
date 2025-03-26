# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        def  backtrack(start,end,path):
            if end==4 and start==len(s) and len(path)==4:
                ans.append(".".join(path))
                return 
            
                 
            for i  in range(start,min(start+3,len(s))):
                d=s[start:i+1] 
                if int(d)>255 or (d[0]=="0" and len(d)>1):
                    continue
                path.append(d)
                backtrack(i+1,end+1,path)

                path.pop()
        backtrack(0,0,[]) 
        return ans 
             

