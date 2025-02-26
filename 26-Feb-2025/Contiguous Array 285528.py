# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curr=0
        prefix=[0]
        deck=defaultdict(list)
        for i  in nums:
            if i==1:
                curr+=1
            else:
                curr-=1
            prefix.append(curr) 
        for i,v  in enumerate(prefix):
            deck[v].append(i+1)
        maxwidth=0  
        
        for i  in deck:
           
            if len(deck[i])>1:
               
                maxwidth=max(maxwidth,deck[i][-1]-deck[i][0])
             
        return maxwidth     