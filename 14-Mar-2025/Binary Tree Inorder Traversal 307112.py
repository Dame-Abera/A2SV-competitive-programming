# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.l=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        return self.l
    def inorder(self,root):
        if not root:
            return []  
        self.inorder(root.left) 
        self.l.append(root.val)   
        self.inorder(root.right)
        return self.l
