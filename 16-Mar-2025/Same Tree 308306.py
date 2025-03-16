# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)
    def dfs(self,left,right):
            if not left and not right:
                return True
            if  not right and left:
                return  False
            if not left and  right:
                return False
            return  left.val==right.val and self.dfs(left.right,right.right)  and self.dfs(left.left,right.left)          