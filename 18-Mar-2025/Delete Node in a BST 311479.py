# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        if root.val>key:
              root.left=self.deleteNode(root.left,key)  
        elif root.val<key:
              root.right=self.deleteNode(root.right,key) 
        else:
            if not root.left:
                return  root.right
            if not root.right:
                return root.left
            else:
                cur=root.right
                while cur.left:
                    cur=cur.left
                print(cur.val)    
                root.val=cur.val   
                root.right=self.deleteNode(root.right,cur.val)            
        return root          
