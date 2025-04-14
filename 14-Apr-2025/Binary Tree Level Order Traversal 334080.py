# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        if root:
          q.append(root)
        res=[]
        while q:
            arr=[]
            l=len(q)
            for i  in range(l):
                s=q.popleft()
                arr.append(s.val)
                if s.left:
                    q.append(s.left)
                if s.right:
                    q.append(s.right)    
            res.append(arr)    
        return res     
                 