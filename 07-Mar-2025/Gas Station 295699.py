# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr=[]
        tot=0
        res=0
        if sum(gas)<sum(cost):
            return -1
        for i   in range(len(gas)):
             arr.append(gas[i]-cost[i])  
        for i,v  in enumerate(arr):
            tot+=v
            if tot<=0:
                res=(i+1)%len(gas)
                tot=0
        return res

