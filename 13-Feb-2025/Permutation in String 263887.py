# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       a=Counter(s1)
       hc=Counter()
       l=0
       for i in range(len(s2)):
            hc[s2[i]]+=1
            
            if  i>=len(s1):
                if hc[s2[l]]==1:
                    del hc[s2[l]]
                else:
                    hc[s2[l]]-=1
                l+=1
            if hc==a:
                return  True   


       return False              


                
       return False          