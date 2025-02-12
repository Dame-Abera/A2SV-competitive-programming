# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        deck=defaultdict(int)
        hset=set()
        res=[]
        for i in s:
            deck[i]+=1
        fl=0    
        for idx,val in enumerate(s):
            hset.add(val)
            if deck[val]==1:
               del deck[val]
            else:
                deck[val]-=1 
            if all(key  not in deck for key in hset):
                 res.append(idx-fl+1)
                 fl=idx+1
                 hset=set()
        return res         
            

