# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right"
class Solution:
    def __init__(self):
        
        self.s=0
        self.flag=False
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
         self.best(root,targetSum)
         return self.flag==True
    def best(self,root,targetSum):
        if not root:
            return 
        self.s+=root.val   
        self.best(root.left,targetSum) 
        self.best(root.right,targetSum)   
       
        if  not root.left and not root.right:
            if self.s==targetSum:
                    self.flag=True
        self.s-=root.val        
