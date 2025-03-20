# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        path=[0 for i  in range(k)]
        print(path)
        fairness=float("inf")
        def  backtrack(start,path):
            nonlocal  fairness
            if start==len(cookies):
               fairness=min(fairness,max(path))
               return 
            for i in range(0,k):
                if  max(path)>=fairness:
                    continue
                path[i]+=cookies[start]
                backtrack(start+1,path)
                path[i]-=cookies[start]
            return fairness    
        return backtrack(0,path)        