# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.prev=self.root
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        r=root
        if not root:
            r=TreeNode(val)
            return r
        prev=root
        while r:
            if r.val>val :
                prev=r
                r=r.left
                
            else:
                prev=r
                r=r.right
                
        print(root)
      
        if prev.val>val:
            prev.left=TreeNode(val)
        else:
            prev.right=TreeNode(val)    
        print(r)
        print(root)  
        return root        