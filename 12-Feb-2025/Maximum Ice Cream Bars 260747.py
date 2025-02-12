# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mas=max(costs)+1
        arr=[0]*mas
        for i in costs:
            arr[i]+=1
        index=0
        for idx,val in enumerate(arr):
            for value in range(val):
                costs[index]=idx
                index+=1
        ptr=0
        res=0
        while  ptr<len(costs) and coins-costs[ptr]>=0 :
             res+=1
             coins-=costs[ptr]
             ptr+=1
            
        return res     
