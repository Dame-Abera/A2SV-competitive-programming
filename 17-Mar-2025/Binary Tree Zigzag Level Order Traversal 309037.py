# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
        self.flag=False
        self.temp=[]
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([root])
        while q:
            self.temp=[]
            for _ in range(len(q)):
                  temp=q.popleft()
                   
                  self.temp.append(temp.val)
                  if temp.left:
                    q.append(temp.left)
                  if temp.right:
                    q.append(temp.right)
            if self.flag:
                print(self.temp)
                self.temp.reverse()
                self.res.append(self.temp) 
            else:
                
                self.res.append(self.temp)        
            self.flag=not self.flag          
        return self.res