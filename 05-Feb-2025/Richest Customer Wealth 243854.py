# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth=0
        for i in accounts:
            maxwealth=max(maxwealth,sum(i))
        return maxwealth    
