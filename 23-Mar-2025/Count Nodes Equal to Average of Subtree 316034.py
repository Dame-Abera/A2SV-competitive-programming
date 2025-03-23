# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def  __init__(self):
        self.count=0
    def averageOfSubtree(self, root: TreeNode) -> int:
       
        def dfs(root):
            if not root:
                return [0,0]

            left=dfs(root.left) 

            right=dfs(root.right) 
           
            if not left[0] and not right[0]:
               
                self.count+=1
           
            if (left[0] or right[0])  and (root.val+right[1] + left[1]) // (left[0] + right[0]+1) == root.val:
               
                self.count+=1

            return [1+right[0]  + left[0],root.val + left[1] + right[1]]

        dfs(root)
        
        return self.count
