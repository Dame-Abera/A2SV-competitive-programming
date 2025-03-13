# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        return self.findWinner([i for i in range(1,n+1)],k ,0)

    def findWinner(self,arr,k,start):  
        if len(arr)==1:
            return arr[0]

        removed=(start+k-1)%len(arr) 
        arr.pop(removed)

        return self.findWinner(arr[:],k,removed)