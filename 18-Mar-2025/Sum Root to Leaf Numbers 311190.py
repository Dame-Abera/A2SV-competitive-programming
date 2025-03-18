# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tot=0
        self.temp=0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sum_to_end(root):
            if not root:
                
                return
           
            self.temp=(self.temp * 10) + root.val 
            
            sum_to_end(root.left) 
            sum_to_end(root.right) 
        
            if not root.right and not root.left:
             self.tot += self.temp
            if self.temp:
                self.temp //= 10
        sum_to_end(root)
        return self.tot
        


        