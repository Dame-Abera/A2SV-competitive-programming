# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
           root.val=[root.val,root.val,root.val]
           self.dfs(root)
           return self.res
    def dfs(self,root):
                if not root: 
                   return
                if root.left:
                    root.left.val=[root.left.val,max(root.val[1],root.left.val),min(root.val[2],root.left.val)]
                if root.right:
                    root.right.val=[root.right.val,max(root.val[1],root.right.val),min(root.val[2],root.right.val)] 
                self.dfs(root.left)
                self.dfs(root.right)
                self.res=max(root.val[1]-root.val[2],self.res)
                print(self.res)

