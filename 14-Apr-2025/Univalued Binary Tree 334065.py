# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
       
        q=deque()
        q.append(root)
        s=set()
        while q:
            cur=q.popleft()
            s.add(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right) 
        return len(s)<=1