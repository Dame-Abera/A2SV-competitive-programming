# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res=0
        deck=defaultdict(int)
        for  i  in answers:
            if  i==0:
                res+=1  
                
                continue
            else:    
                if  i not  in deck:
                    res+=i+1
                    deck[i]=i
                    
                else:
                   if deck[i]==1:
                    del deck[i]
                   else:
                      deck[i]-=1  
                  
        return res