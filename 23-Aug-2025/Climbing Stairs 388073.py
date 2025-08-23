# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
            if n<=1:
              return 1
            return self.climbStairs(n-1)+self.climbStairs(n-2)