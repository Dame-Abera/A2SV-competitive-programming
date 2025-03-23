# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        def  dfs(root):
            nonlocal arr
            if not root:
                return
            dfs(root.left)    
            dfs(root.right)
            arr.append(root.val)
        def  dfs2(root):
            nonlocal arr
            
            if not root:
                return
            dfs2(root.left)    
            dfs2(root.right)
            root.val = hashmap[root.val]  
           
        dfs(root)    
        
        prefix=[]
        curr=0
        arr.sort(reverse=True)
        for  i in range(len(arr)):
            curr +=  arr[i]
            prefix.append(curr)

        hashmap=defaultdict(int)

        for i in range(len(arr)):

              hashmap[arr[i]] = prefix[i] 
          
        dfs2(root)
        
        return root
