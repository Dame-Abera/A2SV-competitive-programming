# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        deck=defaultdict(list)
        for i in range(n):
             deck[i]=[]
        for a,b in edges:
            deck[b].append(a)
        res=[]    
        for i  in deck:
            if len(deck[i])==0:
                res.append(i)
        if len(res)==1:
            return res[0]
        else:
            return -1    
                    
