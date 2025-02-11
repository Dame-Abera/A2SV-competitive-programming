# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        turns=len(piles)//3
        index=len(piles)-2
        res=0
        piles.sort()
        for i in range(turns):
            res+=piles[index]
            print(piles[index])
            index-=2
        return res    
