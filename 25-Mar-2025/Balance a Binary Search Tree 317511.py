# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        def traverse(root):
            if not root:
                return 
            traverse(root.left) 
            traverse(root.right)
            arr.append(root.val)      
        traverse(root)     
        arr.sort() 
        def dfs(left,right):
            if left>right:
                return 
            mid=(left+right)//2
            newroot=TreeNode(arr[mid])  
            newroot.left=dfs(left,mid-1)
            newroot.right=dfs(mid+1,right) 
            return newroot 
        return dfs(0,len(arr)-1)
        
