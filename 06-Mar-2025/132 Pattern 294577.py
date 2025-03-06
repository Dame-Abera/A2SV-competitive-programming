# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=deque()
        mv=nums[0]
        for i in nums:
            
            while stack and stack[-1][0]<i:
                stack.pop()
            if stack and stack[-1][0]>i and i>stack[-1][1]:
                return True    
            stack.append([i,mv])    
            mv=min(mv,i)
        return False        
