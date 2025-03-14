# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack=[]
        self.res=[]
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root):
                if not root:
                  print(root) 
                  print(self.stack) 
                  return 
               
                self.stack.append(str(root.val))  
                helper(root.left) 
                helper(root.right)
                if not root.left and not root.right: 
                   self.res.append("->".join(self.stack))
                if self.stack :
                     self.stack.pop() 
        helper(root)        
        return self.res
        print(res)
        print(stack)


             