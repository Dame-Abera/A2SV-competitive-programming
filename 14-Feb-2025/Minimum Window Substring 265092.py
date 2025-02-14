# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r=0,0
        deck=defaultdict(int)
        c=Counter(t)
        res=""
        while r<len(s):
            deck[s[r]]+=1
            while all(deck[s[l]]>c[s[l]] for i in c) and (l<r and deck[s[l]]>c[s[l]]):
                
                deck[s[l]]-=1
                l+=1
                
            if all(deck[i]>=c[i] for i in c):
                if len(res)==0:
                    res=s[l:r+1]

                if len(s[l:r+1])<len(res):
                    res=s[l:r+1]
                  
            r+=1  
             
        return res    


            
            