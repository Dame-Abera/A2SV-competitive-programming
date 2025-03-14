# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ls=[]
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        rights=self.maxDepth(root.right)
        lefts=self.maxDepth(root.left)
        return 1+max(rights,lefts)
        
        