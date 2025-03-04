# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        deck=defaultdict(int)
        for i  in range(len(bills)):
            if bills[i]==5:
                deck[5]+=1
            elif bills[i]==10:
                deck[10]+=1
                if deck[5]:
                    if deck[5]==1:
                        del deck[5]
                    else:
                        deck[5]-=1
                else:
                    return False        
            else:
                if deck[10] and deck[5]:
                        if deck[10]==1:
                          del deck[10]
                        else:
                            deck[10]-=1
                        if deck[5]==1:
                           del deck[5]
                        else:
                          deck[5]-=1    
                elif  deck[5]>=3:
                    if deck[5]==3:
                        del deck[5]
                    else:
                        deck[5]-=3
                else:    
                    return False
               
        return True                      


